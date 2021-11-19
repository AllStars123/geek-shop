from django.shortcuts import render


def index(request):
    context = {
        'title': 'Geekshop Store'
    }
    return render(request, 'mainapp/index.html', context=context)


def products(request):
    context = {
        'title': 'geekshop'
    }
    return render(request, 'mainapp/products.html', context=context)
