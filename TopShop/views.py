from django.shortcuts import render
from .models import Category, Product, Subcategories

# Create your views here.
class CategoriesView(generic.ListView):
    template_name = 'shop/categories.html'
    context_object_name = 'categories'
    def get_queryset(self):
        return Category.objects.all()

class SubcategoriesView(generic.ListView):
    template_name = 'shop/subcategories.html'
    context_object_name = 'subcategories'
    def get_queryset(self):
        return Subcategory.objects.all()

class ProductsView(generic.ListView):
    template_name = 'shop/products.html'
    context_object_name = 'products'
    def get_queryset(self):
        return Product.objects.all()