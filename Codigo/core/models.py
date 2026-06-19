from django.db import models
from django.contrib.auth.models import User

class Dica(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo


class Exercicio(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.IntegerField()
    instrucoes = models.TextField()

    def __str__(self):
        return self.nome


class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    link = models.URLField()
    categoria = models.CharField(max_length=50, default='Geral')
    data = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.titulo


class Diario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateField(auto_now_add=True)
    humor = models.CharField(max_length=50)

    def __str__(self):
        return f"Diário de {self.usuario.nome}"


class Crise(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField()

    def __str__(self):
        return f"Crise registrada em {self.data}"