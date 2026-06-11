from django.db import models

"""crise"""
class Crise(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    observacao = models.TextField()

    def __str__(self):
        return f"Crise registrada em {self.data}"
