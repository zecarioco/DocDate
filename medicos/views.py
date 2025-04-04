from django.http import HttpResponse

def listar_medicos(request):
    return HttpResponse("Lista de médicos")