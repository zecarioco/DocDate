from django.contrib import admin
from .models import Usuario, Paciente, Medico, Cidade

admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Cidade)