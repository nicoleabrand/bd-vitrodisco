from django.db import models

from core.views import artista, genero, gravadora

class Produto(models.Model):
    nome = models.CharField(max_length=250)
    tracks = models.IntegerField()
    rotacao = models.CharField(max_length=4, blank=True, null=True)
    gramatura = models.CharField(max_length=4, blank=True, null=True)
    tamanho = models.CharField(max_length=6, blank=True, null=True)
    lancamento = models.DateField()
    descricao = models.CharField(max_length=250)
    preco = models.CharField(max_length=6)
    estoque = models.IntegerField()
    artista = models.ForeignKey(artista)
    gravadora = models.ForeignKey(gravadora)
    genero = models.ForeignKey(genero)

    def __str__(self):
        return f"{self.nome}"
# para o field artista e gravadoras, fazer outra tabela e relacionar aqui