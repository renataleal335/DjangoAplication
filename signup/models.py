from django.db import models

class Person(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Não Binário"]
    ]

    nome = models.CharField(max_length=255, null=False)
    endereco = models.CharField(max_length=255, null=False)
    cidade = models.CharField(max_length=255, null=False)
    uf = models.CharField(max_length=2, null=False)
    cep = models.IntegerField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    data_nascimento = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.nome

class Product (models.Model):
    nome = models.CharField(max_length=255, null=False)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    quantidade_produtos = models.IntegerField()
    def __str__(self):
        return self.nome