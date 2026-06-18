from django.shortcuts import render


def login_view(request):
    # Tela de login integrada ao Django (visual + formulario).
    # Autenticacao real (validar usuario/senha, sessao) e tarefa da proxima sprint.
    return render(request, 'core/login.html')


def home(request):
    return render(request, 'core/home.html')


def diario(request):
    return render(request, 'core/diario.html')


def exercicios(request):
    return render(request, 'core/exercicios.html')


def dicas(request):
    return render(request, 'core/dicas.html')


def noticias(request):
    return render(request, 'core/noticias.html')


def crise(request):
    return render(request, 'core/crise.html')
