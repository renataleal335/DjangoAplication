from django.urls import path

from . import views
from .views import ProductList, PersonList, AddSale, SalesList


app_name = 'signup'

urlpatterns = [
    path('create_person/', views.create_person, name='create_person'),

    path('PersonList/', PersonList.as_view(), name="person_list"),
    path('person_delete/<int:id>/', views.person_delete, name='person_delete'),
    path('person_update/<int:id>/', views.person_update, name='person_update'),

    path('product/', views.product, name='product'),

    path('ProductList/', ProductList.as_view(), name="product_list"),
    path('product_delete/<int:id>/', views.product_delete, name='product_delete'),
    path('product_update/<int:id>/', views.product_update, name='product_update'),


   
    path('AddSale/', AddSale.as_view(), name='add_sale'),
    path('SalesList/', SalesList.as_view(), name='sales_list'),
    path('sale_delete/<int:id>/', views.sale_delete, name='sale_delete'),
    path('sale_update/<int:id>/', views.sale_update, name='sale_update'),







]
