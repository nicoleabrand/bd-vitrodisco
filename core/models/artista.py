from django.db import models

class Artista(models.Model):
    nome = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.nome}"
    
#  outra tabela de artista para lincar a disco