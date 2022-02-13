from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse, request
from .forms import UsuarioForm, ProductForm, SalesForm, ItemSaleForm
from django.urls import reverse
from django.template import loader

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Person, SaleItem, Sales, Product
from django.forms import formset_factory

# def profile(request):
# return HttpResponse("Hello, world. You're at the polls index.")


def create_person(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup:person_list')
    else:
        form = UsuarioForm()
    return render(request, "create_person.html", {'form': form})


def sales(request):
    ItemSaleFormSet = formset_factory(ItemSaleForm, extra=1)
    if request.method == 'POST':
        form = SalesForm(request.POST)
        formset = ItemSaleFormSet(request.POST, request.FILES)
        if form.is_valid():
            sales = form.save()
        if formset.is_valid():
            for itemFormSet in formset:
                if itemFormSet.cleaned_data.get('DELETE') and itemFormSet.instance.pk:
                    itemFormSet.instance.delete()
                else:
                    instance = itemFormSet.save(commit=False)
                    instance.sales = sales
                    instance.save()
        return redirect('signup:sales', {'form': form, 'formset': formset})
    else:
        form = SalesForm()
        formset = ItemSaleFormSet()
    return render(request, "signup/sales.html", {'form': form, 'formset': formset})


def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup:product_list')
    else:
        form = ProductForm()
    return render(request, "signup/product.html", {'form': form})


def product_list(request):
    product_list = Product.objects.order_by('-name')
    context = {'product_list': product_list}
    return render(request, 'signup/product_list.html', context)


def sales_list(request):
    sales_list = Sales.objects.order_by('-date_sale')
    context = {'sales_list': sales_list}
    return render(request, 'signup/sales_list.html', context)


def person_list(request):
    persons_list = Person.objects.order_by('-name')
    context = {'persons_list': persons_list}
    return render(request, 'signup/person_list.html', context)


def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    person.delete()
    return redirect('signup:person_list')


def product_delete(request, id):
    person = get_object_or_404(Product, pk=id)
    person.delete()
    return redirect('signup:product_list')


def sale_delete(request, id):
    sale = get_object_or_404(Sales, pk=id)
    sale.delete()
    return redirect('signup:sales_list')


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


def sale_update(request, id):
    ItemSaleFormSet = formset_factory(ItemSaleForm, extra=1)
    sale = get_object_or_404(Sales, pk=id)

    form = SalesForm(instance=sale)
    formset = ItemSaleForm(instance=item)
    if(request.method == 'POST'):
        form = SalesForm(request.POST, instance=sale)
        formset = ItemSaleFormSet(request.POST, instance=item)
        if (form.is_valid()):
            form.save()
            return redirect('signup:sales_list')
        else:
            return render(request, 'signup/edit_sale.html', {'form': form, 'sale': sale, 'formset': formset, 'item': item})
    elif(request.method == 'GET'):
        return render(request, 'signup/edit_sale.html', {'form': form, 'sale': sale})
