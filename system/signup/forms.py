from django import forms
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
        model = Sales
        fields = ["date_sale", "person", "total"]

class ItemSaleForm(forms.ModelForm):
    class Meta:
        model = SaleItem
        fields = ["product", "quantity", "value_product"]

