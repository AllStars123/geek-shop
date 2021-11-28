from django.shortcuts import render
from .models import ProductCategory, Product


def index(request):
    context = {
        'title': 'Geekshop Store'
    }
    return render(request, 'mainapp/index.html', context=context)


def products(request):
    context = {'title': 'geekshop',
               'categories': ProductCategory.objects.all(),
               'products': Product.objects.all()
               }
    return render(request, 'mainapp/products.html', context=context)
