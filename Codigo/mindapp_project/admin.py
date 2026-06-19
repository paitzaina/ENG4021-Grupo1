from django.contrib import admin
# Register your models here.

from core.models import Dica, Exercicio, Noticia, Diario, Crise
admin.site.register(Dica)
admin.site.register(Exercicio)
admin.site.register(Noticia)
admin.site.register(Diario)
admin.site.register(Crise)