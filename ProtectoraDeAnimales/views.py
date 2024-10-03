from django.shortcuts import render
from .models import Animal
from .models import Colaborador
from .models import Protectora

# Create your views here.
def menu(request):
    return render(request,'ProtectoraDeAnimales/menu.html',{})

def lista_animales(request):
    animales = Animal.objects.all()
    return render(request, 'ProtectoraDeAnimales/lista_animales.html',{'animales_mostrar': animales})

def lista_colaboradores(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'ProtectoraDeAnimales/lista_colaboradores.html',{'colaboradores_mostrar':colaboradores})

def lista_protectoras(request):
    protectoras = Protectora.objects.all()
    return render(request, 'ProtectoraDeAnimales/lista_protectoras.html',{'protectoras_mostrar':protectoras})
