from django.contrib.auth.models import AbstractUser
from django.db import models
from medicos.models import Especialidade

class Cidade(models.Model):
    nome = models.CharField(max_length=100)
    estado = models.CharField(max_length=100, null=True, blank=True)
    pais = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        if self.estado and self.pais:
            return f"{self.nome}, {self.estado} - {self.pais}"
        return self.nome

class Usuario(AbstractUser):
    TIPO_USUARIO_CHOICES = [
        ('paciente', 'Paciente'),
        ('medico', 'Médico'),
    ]
    tipo_usuario = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES)
    email = models.EmailField(max_length=255, unique=True)
    cidade = models.ForeignKey(Cidade, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.get_full_name() or self.username


class Paciente(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.usuario.first_name} {self.usuario.last_name}'


class Medico(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    crm = models.CharField(max_length=20, unique=True)
    especialidades = models.ManyToManyField(Especialidade, related_name='medicos')
    clinica = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'{self.usuario.first_name} {self.usuario.last_name} - CRM: {self.crm}'