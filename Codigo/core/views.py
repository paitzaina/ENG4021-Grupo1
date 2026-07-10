from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import date, timedelta
from .models import Exercicio, Dica, Noticia, Diario, Crise


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    erro = None
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        senha = request.POST.get('senha', '').strip()
        user = authenticate(request, username=email, password=senha)
        if user is not None:
            login(request, user)
            return redirect('home')
        erro = 'Email ou senha invalidos.'
    return render(request, 'core/login.html', {'erro': erro})


def cadastro_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    erro = None
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        senha = request.POST.get('senha', '').strip()
        senha2 = request.POST.get('senha2', '').strip()
        if not email or not senha:
            erro = 'Preencha todos os campos.'
        elif senha != senha2:
            erro = 'As senhas nao coincidem.'
        elif User.objects.filter(username=email).exists():
            erro = 'Ja existe uma conta com este email.'
        else:
            user = User.objects.create_user(username=email, email=email, password=senha)
            login(request, user)
            return redirect('home')
    return render(request, 'core/cadastro.html', {'erro': erro})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home(request):
    return render(request, 'core/home.html')


NOMES_DIAS = ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sab', 'Dom']

def _datas_diario():
    hoje = date.today()
    datas = []
    for i in range(0, 6):
        d = hoje - timedelta(days=i)
        if i == 0:
            label = 'Hoje'
        elif i == 1:
            label = 'Ontem'
        else:
            label = NOMES_DIAS[d.weekday()]
        datas.append({
            'data': d,
            'label': label,
            'dia': d.day,
        })
    return datas


@login_required(login_url='login')
def diario(request):
    datas = _datas_diario()
    data_str = request.GET.get('data')
    if data_str:
        try:
            data_selecionada = date.fromisoformat(data_str)
        except ValueError:
            data_selecionada = date.today()
    else:
        data_selecionada = date.today()

    for d in datas:
        d['selecionada'] = d['data'] == data_selecionada

    entradas = Diario.objects.filter(usuario=request.user, data=data_selecionada).order_by('-id')

    return render(request, 'core/diario.html', {
        'datas': datas,
        'data_selecionada': data_selecionada,
        'entradas': entradas,
    })


@login_required(login_url='login')
def diario_criar(request):
    if request.method == 'POST':
        texto = request.POST.get('texto', '').strip()
        humor = request.POST.get('humor', '').strip()
        data_str = request.POST.get('data')
        try:
            data_entrada = date.fromisoformat(data_str)
        except (TypeError, ValueError):
            data_entrada = date.today()
        if texto:
            Diario.objects.create(
                usuario=request.user,
                texto=texto,
                humor=humor,
                data=data_entrada,
            )
        return redirect(f"{reverse('diario')}?data={data_entrada.isoformat()}")
    return redirect('diario')


@login_required(login_url='login')
def diario_editar(request, id):
    entrada = get_object_or_404(Diario, id=id, usuario=request.user)
    if request.method == 'POST':
        entrada.texto = request.POST.get('texto', '').strip()
        entrada.humor = request.POST.get('humor', '').strip()
        entrada.save()
    return redirect(f"{reverse('diario')}?data={entrada.data.isoformat()}")


@login_required(login_url='login')
def diario_excluir(request, id):
    entrada = get_object_or_404(Diario, id=id, usuario=request.user)
    data_entrada = entrada.data
    if request.method == 'POST':
        entrada.delete()
    return redirect(f"{reverse('diario')}?data={data_entrada.isoformat()}")


EXERCICIO_ICONES = {
    'Respiracao': '🫁',
    'Relaxamento': '💪',
    'Meditacao': '🧘',
    'Corpo': '🌿',
    'Alongamento': '🤸',
    'Visualizacao': '🌄',
}

EXERCICIO_ANIMACOES = {
    'Respiracao': 'pulsando',
    'Relaxamento': 'pulsando',
    'Alongamento': 'pulsando',
    'Meditacao': 'brilho',
    'Corpo': 'brilho',
    'Visualizacao': 'brilho',
}


def exercicios(request):
    lista_exercicios = list(Exercicio.objects.all())
    for ex in lista_exercicios:
        ex.icone = EXERCICIO_ICONES.get(ex.tipo, '🫁')
        ex.animacao = EXERCICIO_ANIMACOES.get(ex.tipo, 'pulsando')
    return render(request, 'core/exercicios.html', {'exercicios': lista_exercicios})


def dicas(request):
    categorias = ['Ansiedade', 'Estresse', 'Foco e estudos', 'Sono']
    categoria_selecionada = request.GET.get('categoria', categorias[0])
    lista_dicas = Dica.objects.filter(categoria=categoria_selecionada)
    return render(request, 'core/dicas.html', {
        'dicas': lista_dicas,
        'categorias': categorias,
        'categoria_selecionada': categoria_selecionada,
    })


def noticias(request):
    lista_noticias = Noticia.objects.all().order_by('-data')
    noticia_destaque = Noticia.objects.filter(destaque=True).first()
    return render(request, 'core/noticias.html', {
        'noticias': lista_noticias,
        'noticia_destaque': noticia_destaque,
    })


def noticia_detalhe(request, id):
    noticia = get_object_or_404(Noticia, id=id)
    return render(request, 'core/noticia_detalhe.html', {'noticia': noticia})


@login_required(login_url='login')
def crise(request):
    Crise.objects.create(usuario=request.user, observacao='')
    return render(request, 'core/crise.html')


def csrf_failure(request, reason=""):
    return render(request, 'core/csrf_failure.html', status=403)
