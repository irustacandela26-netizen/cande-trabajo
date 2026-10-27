from django.shortcuts import render
# Create your views here.

def inicio(request):
    return render(request, 'trivia/inicio.html')


def pregunta1(request):
    return render(request, 'trivia/pregunta1.html')


def pregunta2(request):
    return render(request, 'trivia/pregunta2.html')


def pregunta3(request):
    return render(request, 'trivia/pregunta3.html')

def pregunta4(request):
    return render(request, 'trivia/pregunta4.html')


def game_over(request):
    return render(request, 'trivia/game_over.html')


def win(request):
    return render(request, 'trivia/win.html')

