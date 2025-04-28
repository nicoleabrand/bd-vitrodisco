from django.db import models

class Endereco(models.Model):
    Rua = models.CharField(max_length=250)
    NumeroCasa = models.IntegerField()
    Bairro = models.CharField(max_length=50)
    Cidade = models.CharField(max_length=50)
    Pais = models.CharField(max_length=50)
    CEP = models.IntegerField()

    def __str__(self):
        return f"{self.nome}"