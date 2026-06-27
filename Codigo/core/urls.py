from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('cadastro/', views.cadastro_view, name='cadastro'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('diario/', views.diario, name='diario'),
    path('diario/novo/', views.diario_criar, name='diario_criar'),
    path('diario/<int:id>/editar/', views.diario_editar, name='diario_editar'),
    path('diario/<int:id>/excluir/', views.diario_excluir, name='diario_excluir'),
    path('exercicios/', views.exercicios, name='exercicios'),
    path('dicas/', views.dicas, name='dicas'),
    path('noticias/', views.noticias, name='noticias'),
    path('noticias/<int:id>/', views.noticia_detalhe, name='noticia_detalhe'),
    path('crise/', views.crise, name='crise'),
]
