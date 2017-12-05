from django.shortcuts import render
from .models import Category, Product


def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'catalog/product_list.html', context)


def category(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    context = {
        'current_category': category,
        'product_list': products,
    }
    return render(request, 'catalog/category.html', context)


def product(request, slug):
    product = Product.objects.get(slug=slug)
    context = {
        'product': product,
    }
    return render(request, 'catalog/product.html', context)
