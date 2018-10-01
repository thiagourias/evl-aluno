from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request, 'home.html')

def meusCursos(request):
    return render(request, 'meusCursos.html')

def certificados(request):
    return render(request, 'certificados.html')

def comprovantes(request):
    return render(request, 'comprovantes.html')