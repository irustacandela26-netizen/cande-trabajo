from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, 'historia/inicio.html')

def bosque(request):
    return render(request, 'historia/bosque.html')


def torre(request):
    return render(request, 'historia/torre.html')


def final_bueno(request):
    return render(request, 'historia/final_bueno.html')


def final_malo(request):
    return render(request, 'historia/final_malo.html')

def isla(request):
    return render(request, 'historia/isla.html')

def tesoro(request):
    return render(request, 'historia/tesoro.html')

from django.shortcuts import render, get_object_or_404
from .models import Escena

def escena(request, slug):
    escena = get_object_or_404(Escena, slug=slug)
    opciones = escena.opciones_salida.select_related("escena_destino").all()
    return render(request, "historia/escena.html", {
        'escena': escena,
        'opciones': opciones,
    })

