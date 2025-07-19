from django.urls import path, include
from . import views
from rest_framework import routers
from .api import EmployeeViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth import get_user_model
from rest_framework import permissions

# Router DRF pour l'API Employee
router = routers.DefaultRouter()
router.register(r'api/employees', EmployeeViewSet)

# Swagger schema view
schema_view = get_schema_view(
    openapi.Info(
        title="Employee API",
        default_version='v1',
        description="API de gestion des employés (import, CRUD, export)",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('importer/', views.importer_excel, name='importer_excel'),
    path('employees/', views.liste_employees, name='liste_employees'),
    path('employee/<int:pk>/modifier/', views.modifier_employee, name='modifier_employee'),
    path('employee/creer/', views.creer_employee, name='creer_employee'),
    path('exporter/', views.exporter_excel, name='exporter_excel'),
    # API REST
    path('', include(router.urls)),
    # Documentation Swagger et Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]