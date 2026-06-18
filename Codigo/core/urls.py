from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),
    path('diario/', views.diario, name='diario'),
    path('exercicios/', views.exercicios, name='exercicios'),
    path('dicas/', views.dicas, name='dicas'),
    path('noticias/', views.noticias, name='noticias'),
    path('crise/', views.crise, name='crise'),
]
