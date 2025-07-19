from django import forms
from .models import Employee

class ImportExcelForm(forms.Form):
    fichier_excel = forms.FileField(label='Sélectionnez un fichier Excel')

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'date_naissance': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'salaire': forms.NumberInput(attrs={'step': '0.01', 'class': 'form-control', 'placeholder': 'Montant en FCFA'}),
        }
        labels = {
            'salaire': 'Salaire (FCFA)',
        }