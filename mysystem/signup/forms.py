from dataclasses import field
from django import forms
from django.forms import modelformset_factory
from .models import *


class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["name", "address", "city", "uf", "cep", "sex", "birth_date"]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "value", "quantity_products"]


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sale
        fields = ["date_sale", "person", "total"]

# class ItemSaleForm(forms.ModelForm):
#     class Meta:
#         model = SaleItem
#         fields = ["product", "sale", "quantity", "value_product"]


ItemFormSet = modelformset_factory(SaleItem, fields=(
    "product", "sale", "quantity", "value_product"), extra=1)
