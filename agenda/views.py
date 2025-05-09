from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .models import Consulta
from usuarios.models import Paciente, Usuario, Medico
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
        paciente = get_object_or_404(Usuario, id=request.POST.get('paciente'))
        medico = get_object_or_404(Medico, id=request.POST.get('medico'))
        
        consulta.paciente = paciente
        consulta.medico = medico
        consulta.data_consulta = request.POST.get('data_consulta')
        consulta.status = request.POST.get('status')
        
        consulta.save()
        
        return redirect('listar_consultas')

    pacientes = Usuario.objects.filter(tipo_usuario='paciente')
    medicos = Medico.objects.all()
    return render(request, 'agendar_consulta.html', {
        'consulta': consulta,
        'medico': consulta.medico,
        'pacientes': pacientes,
        'medicos': medicos
    })


def excluir_consulta(request, consulta_id):
    consulta = get_object_or_404(Consulta, id=consulta_id)
    if request.method == 'POST':
        consulta.delete()
        return redirect('listar_consultas')
    return render(request, 'confirmar_exclusao.html', {'consulta': consulta})

@login_required
def agendar_consulta(request, medico_id):
    medico = get_object_or_404(Medico, id=medico_id)

    try:
        paciente = request.user.paciente
    except Paciente.DoesNotExist:
        return redirect('listar_consultas')
    
    if request.method == 'POST':
        paciente = request.user
        data_consulta = request.POST.get('data_consulta')
        status = request.POST.get('status')
        
        if data_consulta:
            data_consulta = timezone.make_aware(timezone.datetime.fromisoformat(data_consulta))

        consulta = Consulta.objects.create(
            medico=medico,
            paciente=paciente,
            data_consulta=data_consulta,
            status=status
        )
        
        return redirect('listar_consultas')

    return render(request, 'agendar_consulta.html', {'medico': medico})