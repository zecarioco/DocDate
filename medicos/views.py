from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from medicos.models import Especialidade
from usuarios.models import Cidade, Medico
import unicodedata

def listar_medicos(request):
    return HttpResponse("Lista de médicos")

def normalize(texto):
    if texto:
        return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('utf-8').lower()
    return ''

def buscar_medicos(request):
    nome = request.GET.get('q')
    especialidade_id = request.GET.get('especialidade')
    cidade_id = request.GET.get('cidade')

    medicos = Medico.objects.all()

    if nome:
        nome_normalizado = normalize(nome)
        medicos = [m for m in medicos if nome_normalizado in normalize(f"{m.usuario.first_name} {m.usuario.last_name}")]

    if especialidade_id:
        medicos = [m for m in medicos if str(especialidade_id) in [str(e.id) for e in m.especialidades.all()]]

    if cidade_id:
        medicos = [m for m in medicos if m.usuario.cidade and str(m.usuario.cidade.id) == cidade_id]

    especialidades = Especialidade.objects.all()
    cidades = Cidade.objects.all()

    return render(request, 'busca.html', {
        'medicos': medicos,
        'especialidades': especialidades,
        'cidades': cidades,
    })

def perfil_medico_view(request, medico_id):
    medico = get_object_or_404(Medico, id=medico_id)
    return render(request, 'perfil_medico.html', {'medico': medico})