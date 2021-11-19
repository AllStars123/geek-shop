from django.urls import path

from mainapp.views import index, products

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
]
