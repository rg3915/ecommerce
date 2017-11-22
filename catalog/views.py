from django.shortcuts import render
from .models import Product


def product_list(request):

    return render(request, 'catalog/product_list.html')


def product(request):

    return render(request, 'catalog/product.html')
