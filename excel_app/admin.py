from django.contrib import admin
from .models import Employee

# Enregistrement du modèle Employee dans l'admin
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'salaire')
    search_fields = ('nom', 'prenom', 'email')
