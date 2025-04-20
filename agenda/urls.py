from django.urls import path
from . import views

urlpatterns = [
    path('consultas/', views.listar_consultas, name='listar_consultas'),
    path('consultas/editar/<int:consulta_id>/', views.editar_consulta, name='editar_consulta'),
    path('consultas/excluir/<int:consulta_id>/', views.excluir_consulta, name='excluir_consulta'),
    path('consultas/nova/<int:medico_id>/', views.agendar_consulta, name='agendar_consulta'),
]