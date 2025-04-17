from django.urls import path
from . import views

urlpatterns = [
    path('medicos/', views.listar_medicos, name='listar_medicos'),
    path('buscar/', views.buscar_medicos, name='buscar_medicos'),
]