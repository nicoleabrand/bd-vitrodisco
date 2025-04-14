from django.db import models

class FormaPagamento(models.Model):
    numeroCartao = models.CharField(max_length=16)
    nomeTitular = models.CharField(max_length=150)
    dataValidade = models.DateField()
    codigoSeguranca = models.CharField(max_length=3)   

    def __str__(self):
        return f"{self.nome}"
