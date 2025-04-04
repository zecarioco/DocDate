from django.shortcuts import render, get_object_or_404, redirect
from .models import Consulta
from usuarios.models import Usuario, Medico
from django.contrib.auth.decorators import login_required

@login_required
def listar_consultas(request):
    usuario = request.user

    if usuario.tipo_usuario == 'medico':
        consultas = Consulta.objects.filter(medico=usuario.medico)
    else:
        consultas = Consulta.objects.filter(paciente=usuario)

    return render(request, 'listar_consultas.html', {'consultas': consultas})

def criar_consulta(request):
    if request.method == 'POST':
        paciente_id = request.POST.get('paciente')
        medico_id = request.POST.get('medico')
        data_consulta = request.POST.get('data_consulta')
        status = request.POST.get('status')

        paciente = get_object_or_404(Usuario, id=paciente_id, tipo_usuario='paciente')
        medico = get_object_or_404(Medico, id=medico_id)

        Consulta.objects.create(paciente=paciente, medico=medico, data_consulta=data_consulta, status=status)
        return redirect('listar_consultas')

    pacientes = Usuario.objects.filter(tipo_usuario='paciente')
    medicos = Medico.objects.all()
    return render(request, 'form_consulta.html', {'pacientes': pacientes, 'medicos': medicos})

def editar_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)

    if request.method == 'POST':
        consulta.paciente = get_object_or_404(Usuario, id=request.POST.get('paciente'))
        consulta.medico = get_object_or_404(Medico, id=request.POST.get('medico'))
        consulta.data_consulta = request.POST.get('data_consulta')
        consulta.status = request.POST.get('status')
        consulta.save()
        return redirect('listar_consultas')

    pacientes = Usuario.objects.filter(tipo_usuario='paciente')
    medicos = Medico.objects.all()
    return render(request, 'form_consulta.html', {'consulta': consulta, 'pacientes': pacientes, 'medicos': medicos})

def excluir_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    if request.method == 'POST':
        consulta.delete()
        return redirect('listar_consultas')
    return render(request, 'confirmar_exclusao.html', {'consulta': consulta})