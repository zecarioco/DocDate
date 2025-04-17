from django.http import HttpResponse
from django.shortcuts import render
from usuarios.models import Medico

def listar_medicos(request):
    return HttpResponse("Lista de médicos")

def buscar_medicos(request):
    query = request.GET.get('q', '')
    medicos = []

    if query:
        medicos = Medico.objects.filter(
            usuario__first_name__icontains=query
        ) | Medico.objects.filter(
            usuario__last_name__icontains=query
        )

    context = {
        'medicos': medicos.distinct(),
        'query': query,
    }
    return render(request, 'busca.html', context)