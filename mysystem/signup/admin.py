
from django.contrib import admin

from .models import Person, Product, Sale, SaleItem

admin.site.register(Person)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(SaleItem)

