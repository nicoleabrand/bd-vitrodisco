from django.db import models

class Gravadora(models.Model):
    nome = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.nome}"

# Tabela das gravadoras para serem lincados a disco, uma gravadora pode ter vários discos
