from django.urls import path
from .views import home_view, login_view, register_view, logout_view, editar_perfil_view, perfil_view

urlpatterns = [
    path('', home_view, name='home'),
    path('login/', login_view, name='login'),
    path('cadastro/', register_view, name='cadastro'),
    path('logout/', logout_view, name='logout'),
    path('perfil/', perfil_view, name='perfil'),
    path('perfil/editar/', editar_perfil_view, name='editar_perfil'),
]