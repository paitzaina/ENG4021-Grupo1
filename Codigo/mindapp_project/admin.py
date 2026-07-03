# Register your models here.

from django.contrib import admin
from core.models import Dica, Exercicio, Noticia, Diario, Crise


@admin.register(Dica)
class DicaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria')
    list_filter = ('categoria',)
    search_fields = ('titulo', 'descricao')


@admin.register(Exercicio)
class ExercicioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'duracao')
    list_filter = ('tipo',)
    search_fields = ('nome', 'instrucoes')


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'data', 'destaque')
    list_filter = ('categoria', 'destaque')
    search_fields = ('titulo', 'conteudo')


@admin.register(Diario)
class DiarioAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data', 'humor')
    list_filter = ('humor',)


@admin.register(Crise)
class CriseAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'data')
