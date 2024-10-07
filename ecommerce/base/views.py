# views.py

from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html')

# This function name should be lowercase
def products(request):
    products = Product.objects.all()  # Fetch all products from the database
    context = {
        'products': products
    }
    return render(request, 'base/products.html', context)