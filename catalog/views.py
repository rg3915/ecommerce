from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)


def product(request):
    return render(request, 'catalog/product.html')
