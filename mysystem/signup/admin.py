
from django.contrib import admin

from .models import Person, Product, Sales, SaleItem

admin.site.register(Person)
admin.site.register(Product)
admin.site.register(Sales)
admin.site.register(SaleItem)

