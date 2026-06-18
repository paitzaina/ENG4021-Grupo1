from django.db import models


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
