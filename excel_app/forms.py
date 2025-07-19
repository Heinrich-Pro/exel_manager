from django import forms
from .models import Employee

class ImportExcelForm(forms.Form):
    fichier_excel = forms.FileField(label='Sélectionnez un fichier Excel')

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'