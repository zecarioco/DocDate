from django.db import models
from usuarios.models import Usuario
from usuarios.models import Medico

class Consulta(models.Model):
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='consultas', limit_choices_to={'tipo_usuario': 'paciente'})
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='consultas')
    data_consulta = models.DateTimeField()
    status = models.CharField(
        max_length=20, 
        choices=[('agendada', 'Agendada'), ('cancelada', 'Cancelada'), ('realizada', 'Realizada')], 
        default='agendada'
    )

    def __str__(self):
        return f'Consulta: {self.paciente.get_full_name()} com {self.medico.usuario.get_full_name()} - {self.data_consulta.strftime("%d/%m/%Y %H:%M")}'