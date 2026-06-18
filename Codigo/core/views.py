from django.shortcuts import render
from .models import Exercicio, Dica, Noticia


def login_view(request):
    # Tela de login integrada ao Django (visual + formulario).
    # Autenticacao real (validar usuario/senha, sessao) e tarefa da proxima sprint.

    return render(request, 'core/login.html')


def home(request):
    return render(request, 'core/home.html')


def diario(request):
    return render(request, 'core/diario.html')


def exercicios(request):
    lista_exercicios = Exercicio.objects.all()
    return render(request, 'core/exercicios.html', {'exercicios': lista_exercicios})


def dicas(request):
    lista_dicas = Dica.objects.all()
    return render(request, 'core/dicas.html', {'dicas': lista_dicas})


def noticias(request):
    lista_noticias = Noticia.objects.all()
    return render(request, 'core/noticias.html', {'noticias': lista_noticias})


def crise(request):
    return render(request, 'core/crise.html')
