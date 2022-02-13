from django.db import models
from datetime import datetime


class Person(models.Model):
    SEX_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Não Binário"]
    ]

    name = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    city = models.CharField(max_length=255, null=False)
    uf = models.CharField(max_length=2, null=False)
    cep = models.FloatField()
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    birth_date = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Product (models.Model):
    name = models.CharField(max_length=255, null=False)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    quantity_products = models.FloatField()

    def __str__(self):
        return self.name


class Sales (models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    date_sale = models.DateField(default=datetime.today)
    total = models.FloatField()


class SaleItem (models.Model):
    product = models.CharField(max_length=255, null=False)
    quantity = models.FloatField()
    value_product = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.product
