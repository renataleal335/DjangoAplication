from django.urls import path

from . import views

app_name = 'signup'

urlpatterns = [
    path('', views.index, name='index'),
    path('person_list/', views.person_list, name='person_list'),
    path('person_delete/<int:id>/', views.person_delete, name='person_delete'),
    path('editar/<int:id>/', views.person_update, name='person_update'),
    
    path('product/', views.product, name='product'),
    path('product_list/', views.product_list, name='product_list'),
    path('product_delete/<int:id>/', views.product_delete, name='product_delete'),
    path('update/<int:id>/', views.product_update, name='product_update'),
    
    path('sales/', views.sales, name='sales'),
    path('sales_list/', views.sales_list, name='sales_list'),
   

   

]