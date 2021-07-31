from django.shortcuts import render
from .models import Category, Product
import requests

def products(request):
    categories = Category.objects.all()
    products =  Product.objects.all()
    for product in products:
        print(product.category.name)
    return render(request, 'products/products.html',{'categories':categories,'products': products})