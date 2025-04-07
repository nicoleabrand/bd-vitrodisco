from django.db import models

class Disco(models.Model):
    nome = models.CharField(max_length=250)
    tracks = models.IntegerField()
    rotacao = models.CharField(max_length=4)
    gramatura = models.CharField(max_length=4)
    tamanho = models.CharField(max_length=6)
    lancamento = models.DateField()
    descricao = models.CharField(max_length=250)
    preco = models.CharField(max_length=6)
    estoque = models.IntegerField()

    def __str__(self):
        return f"{self.nome}"
# para o field artista e gravadoras, fazer outra tabela e relacionar aqui