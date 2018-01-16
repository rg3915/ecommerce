from django.contrib import admin
from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created')
    search_fields = ('name', 'slug')
    list_filter = ('created', 'modified')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'category', 'created')
    search_fields = ('name', 'slug', 'category__name')
    list_filter = ('created', 'modified', 'category')
