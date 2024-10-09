from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'base/home.html', context)

def room(request):
    return render(request, 'base/room.html')

def login_view(request):  # Renamed to avoid conflict with Django's built-in login
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
                form.add_error(None, 'Invalid credentials')
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

@login_required
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

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if item already in cart
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    messages.success(request, f'{product.name} was added to your cart!')
    return redirect('home')

@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get(user=request.user)
    cart_item = CartItem.objects.get(cart=cart, product=product)
    cart_item.delete()

    return redirect('cart_detail')

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    context = {
        'cart': cart
    }
    return render(request, 'base/cart_detail.html', context)

def update_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = Cart.objects.get(user=request.user)
    
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()

    return redirect('cart_detail')