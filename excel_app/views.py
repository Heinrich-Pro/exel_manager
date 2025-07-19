import pandas as pd
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Employee
from .forms import ImportExcelForm, EmployeeForm
from django.contrib import messages
from io import BytesIO


def accueil(request):
    return render(request, 'excel_app/accueil.html')


def importer_excel(request):
    if request.method == 'POST':
        form = ImportExcelForm(request.POST, request.FILES)
        if form.is_valid():
            fichier_excel = request.FILES['fichier_excel']

            try:
                # Lire le fichier Excel avec pandas
                df = pd.read_excel(fichier_excel)

                # Convertir les noms de colonnes en minuscules et remplacer les espaces
                df.columns = df.columns.str.lower().str.replace(' ', '_')

                # Liste des champs attendus
                champs_attendus = ['nom', 'prenom', 'email', 'telephone', 'date_naissance', 'salaire']

                # Vérifier que les colonnes nécessaires sont présentes
                for champ in champs_attendus:
                    if champ not in df.columns:
                        messages.error(request, f"La colonne '{champ}' est manquante dans le fichier Excel.")
                        return redirect('importer_excel')

                # Parcourir les lignes du DataFrame et créer les employés
                for _, row in df.iterrows():
                    Employee.objects.update_or_create(
                        email=row['email'],
                        defaults={
                            'nom': row['nom'],
                            'prenom': row['prenom'],
                            'telephone': row.get('telephone', ''),
                            'date_naissance': row.get('date_naissance', None),
                            'salaire': row.get('salaire', None),
                        }
                    )

                messages.success(request, 'Les données ont été importées avec succès!')
                return redirect('liste_employees')

            except Exception as e:
                messages.error(request, f"Une erreur s'est produite: {str(e)}")
    else:
        form = ImportExcelForm()

    return render(request, 'excel_app/importer.html', {'form': form})


def liste_employees(request):
    employees = Employee.objects.all().order_by('nom')
    return render(request, 'excel_app/liste.html', {'employees': employees})


def modifier_employee(request, pk):
    employee = get_object_or_404(Employee, pk=pk)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employé mis à jour avec succès!')
            return redirect('liste_employees')
    else:
        form = EmployeeForm(instance=employee)

    return render(request, 'excel_app/modifier.html', {'form': form, 'employee': employee})


def creer_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employé créé avec succès!')
            return redirect('liste_employees')
    else:
        form = EmployeeForm()
    return render(request, 'excel_app/modifier.html', {'form': form, 'employee': None, 'creation': True})


def exporter_excel(request):
    # Récupérer tous les employés
    employees = Employee.objects.all().values(
        'nom', 'prenom', 'email', 'telephone', 'date_naissance', 'salaire'
    )

    # Créer un DataFrame pandas
    df = pd.DataFrame.from_records(employees)

    # Créer un fichier Excel en mémoire
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Employees', index=False)
    output.seek(0)

    # Créer la réponse HTTP avec le fichier Excel
    response = HttpResponse(
        output.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=employees_export.xlsx'

    return response


def supprimer_employee(request, pk):
    from django.urls import reverse
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employé supprimé avec succès!')
        return redirect('liste_employees')
    return render(request, 'excel_app/supprimer.html', {'employee': employee})