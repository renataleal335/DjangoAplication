from django.urls import path

from . import views

app_name = 'signup'

urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product, name='product'),
    path('product_list/', views.product_list, name='product_list'),
    path('results/', views.results, name='results'),
    path('person_delete/<int:id>/', views.person_delete, name='person_delete'),
    path('product_delete/<int:id>/', views.product_delete, name='product_delete'),
    path('editar/<int:id>/', views.person_update, name='person_update'),
    path('update/<int:id>/', views.product_update, name='product_update'),
    

]