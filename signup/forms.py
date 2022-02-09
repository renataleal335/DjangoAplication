from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ["nome", "endereco", "cidade", "uf", "cep", "sexo", "data_nascimento"]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["nome", "valor", "quantidade_produtos"]