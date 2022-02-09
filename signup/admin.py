from django.contrib import admin

from .models import Person
from .models import Product

admin.site.register(Person)
admin.site.register(Product)
