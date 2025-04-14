from django.db import models

class Genero(models.Model):
    nome = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.nome}"