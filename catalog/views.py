from django.shortcuts import render
from django.views import generic
from .models import Category, Product


def product_list(request):
    products = Product.objects.all()
    context = {'product_list': products}
    return render(request, 'catalog/product_list.html', context)


class ProductListView(generic.ListView):
    model = Product
    template_name = 'catalog/product_list.html'

product_list = ProductListView.as_view()


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
