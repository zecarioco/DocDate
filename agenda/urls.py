from django.urls import path
from . import views

urlpatterns = [
    path('consultas/', views.listar_consultas, name='listar_consultas'),
    path('consultas/nova/', views.criar_consulta, name='criar_consulta'),
    path('consultas/editar/<int:consulta_id>/', views.editar_consulta, name='editar_consulta'),
    path('consultas/excluir/<int:consulta_id>/', views.excluir_consulta, name='excluir_consulta'),
]