from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Dica(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    categoria = models.CharField(max_length=50, default='Geral')

    def __str__(self):
        return self.titulo


class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.IntegerField()
    instrucoes = models.TextField()
    tipo = models.CharField(max_length=30, default='Respiracao')

    def __str__(self):
        return self.nome


class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    link = models.URLField()
    categoria = models.CharField(max_length=50, default='Geral')
    data = models.DateField(null=True, blank=True)
    destaque = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo


class Diario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    texto = models.TextField()
    data = models.DateField(default=date.today)
    humor = models.CharField(max_length=50, blank=True)

    def __str__(self):
        nome = self.usuario.username if self.usuario else "anonimo"
        return f"Diario de {nome} em {self.data}"


class Crise(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField()

    def __str__(self):
        return f"Crise registrada em {self.data}"