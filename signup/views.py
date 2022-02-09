from django.shortcuts import render

from django.http import HttpResponse, HttpResponseRedirect, request
from .forms import UsuarioForm
from .forms import ProductForm
from django.urls import reverse
from django.template import loader

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import Person
from .models import Product


def index(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signup:results')
    else:
        form = UsuarioForm()
    return render(request, "index.html", {'form': form})


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
    product_list = Product.objects.order_by('-nome')
    context = {'product_list': product_list}
    return render(request, 'signup/product_list.html', context)


def results(request):
    persons_list = Person.objects.order_by('-nome')
    context = {'persons_list': persons_list}
    return render(request, 'signup/results.html', context)


def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)
    person.delete()
    return redirect('signup:results')

def product_delete(request, id):
    person = get_object_or_404(Product, pk=id)
    person.delete()
    return redirect('signup:product_list')


def product_update(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(instance=product)
    if(request.method == 'POST'):
        form = ProductForm(request.POST, instance=product)
        if(form.is_valid()):
            form.save()
            return redirect ('signup:product_list')
        else:
            return render(request, 'signup/edit_product.html', {'form' : form, 'product' : product})
    elif(request.method == 'GET'):
        return render (request, 'signup/edit_product.html', {'form' : form, 'product' : product })
    form.save()



def person_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = UsuarioForm(instance=person)
    if(request.method == 'POST'):
        form = UsuarioForm(request.POST, instance=person)
        if(form.is_valid()):
            form.save()
            return redirect('signup:results')
        else:
            return render(request, 'signup/edit_person.html', {'form': form, 'person': person})
    elif(request.method == 'GET'):
        return render(request, 'signup/edit_person.html', {'form': form, 'person': person})
    form.save()
