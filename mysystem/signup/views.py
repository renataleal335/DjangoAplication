from datetime import datetime
from pyexpat import model
from re import template
from django.shortcuts import render
from django.http import HttpResponse, request
from .forms import UsuarioForm, ProductForm, SalesForm, ItemFormSet
from django.urls import reverse
from django.template import loader

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Person, SaleItem, Sale, Product
from django.forms import inlineformset_factory
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy


def create_person(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup:person_list')
    else:
        form = UsuarioForm()
    return render(request, "create_person.html", {'form': form})


class PersonList(ListView):
    model = Person
    template_name = "person_list.html"


def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = UsuarioForm(instance=person)
    if(request.method == 'POST'):
        form = UsuarioForm(request.POST, instance=person)
        if(form.is_valid()):
            form.save()
            return redirect('signup:person_list')
        else:
            return render(request, 'signup/edit_person.html', {'form': form, 'person': person})
    elif(request.method == 'GET'):
        return render(request, 'signup/edit_person.html', {'form': form, 'person': person})
    form.save()


def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    person.delete()
    return redirect('signup:person_list')


def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup:product_list')
    else:
        form = ProductForm()
    return render(request, "signup/product.html", {'form': form})


class ProductList(ListView):
    model = Product
    template_name = "product_list.html"


def product_update(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(instance=product)
    if(request.method == 'POST'):
        form = ProductForm(request.POST, instance=product)
        if(form.is_valid()):
            form.save()
            return redirect('signup:product_list')
        else:
            return render(request, 'signup/edit_product.html', {'form': form, 'product': product})
    elif(request.method == 'GET'):
        return render(request, 'signup/edit_product.html', {'form': form, 'product': product})
    form.save()


def product_delete(request, id):
    person = get_object_or_404(Product, pk=id)
    person.delete()
    return redirect('signup:product_list')


# def sale(request):
#     ItemSaleFormSet = formset_factory(ItemSaleForm, extra=1)

#     if request.method == 'POST':
#         form = SalesForm(request.POST)
#         sale = form
#         formset = ItemSaleFormSet(request.POST, request.FILES)
#         if form.is_valid():
#             sale = form.save()
#         if formset.is_valid():
#             for itemFormSet in formset:
#                 if itemFormSet.cleaned_data.get('DELETE') and itemFormSet.instance.pk:
#                     itemFormSet.instance.delete()
#                 else:
#                     instance = itemFormSet.save(commit=False)
#                     instance.sale = sale
#                     instance.save()
#         return redirect('signup:SalesList')
#     else:
#         form = SalesForm()
#         formset = ItemSaleFormSet()
#     return render(request, "signup/sales.html", {'form': form, 'formset': formset})

class AddSale(TemplateView):
    template_name = "signup/sales.html"

    def get(self, request):
        form = SalesForm(request.POST)
        formset = ItemFormSet(queryset=SaleItem.objects.none())
        return self.render_to_response({'formset': formset, 'form': form})

    def post(self, request):
        form = SalesForm(data=self.request.POST)
        formset = ItemFormSet(data=self.request.POST)
        if form.is_valid():
            sale = form.save()
        if formset.is_valid():
            for itemFormSet in formset:
                if itemFormSet.cleaned_data.get('DELETE') and itemFormSet.instance.pk:
                    itemFormSet.instance.delete()
                else:
                    instance = itemFormSet.save(commit=False)
                    instance.sale = sale
                    instance.save()
                    return redirect('signup:sales_list')
        return self.render_to_response({'formset': formset, 'form': form})


class SalesList(ListView):
    model = Sale
    template_name = "signup/sales_list.html"


def sale_delete(request, id):
    sale = get_object_or_404(Sale, pk=id)
    sale.delete()
    return redirect('signup:sales_list')


def sale_update(request, id):
    sale = get_object_or_404(Sale, pk=id)

    form = SalesForm(instance=sale)
    formset = ItemFormSet()

    if(request.method == 'POST'):
        form = SalesForm(request.POST, instance=sale)
        formset = ItemFormSet(request.POST, request.FILES, instance=sale)

        if (form.is_valid() and formset.is_valid()):
            form.save()
            formset.save()

            return redirect('signup:sales_list')
        else:
            return render(request, 'signup/edit_sale.html', {'form': form, 'formset': formset, 'sale': sale, })
    elif(request.method == 'GET'):
        return render(request, 'signup/edit_sale.html', {'form': form, 'formset': formset,  'sale': sale})
