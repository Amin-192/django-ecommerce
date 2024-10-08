from django.shortcuts import render, redirect
from .models import Product
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import auth

def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html')

def login_view(request):  # Renamed to avoid conflict
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)  # Use the built-in login function
                return redirect('home')
            else:
                return redirect('login')
    context = {'loginForm': form}
    return render(request, 'base/login.html', context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    context = {'registerForm': form}
    return render(request, 'base/register.html', context)

def dashboard(request):
    return render(request, 'base/dashboard.html')

def products(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'base/products.html', context)


def user_logout(request):
    logout(request)
    return redirect('home')