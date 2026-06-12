from django.db import models

"""diario"""
class Diario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateField(auto_now_add=True)
    humor = models.CharField(max_length=50)

    def __str__(self):
        return f"Diário de {self.usuario.nome}"
