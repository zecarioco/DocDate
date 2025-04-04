from django.urls import path
from .views import listar_medicos

urlpatterns = [
    path('medicos/', listar_medicos, name='listar_medicos'),
]