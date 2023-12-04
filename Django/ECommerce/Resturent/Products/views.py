from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem
from django.contrib.auth.decorators import login_required
from . import models
from django.contrib.auth.decorators import login_required

def home(request):
    products = models.Product.objects.all()
    return render(request, 'products.html', {'products': products})


@login_required(login_url='/admin/login/')

@login_required(login_url='/admin/login')

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    return redirect('/viewcart')

@login_required(login_url='/admin/login/')
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )

    if not created and cart_item.quantity > 0:
        cart_item.quantity -= 1
        cart_item.save()

    if cart_item.quantity == 0:
        cart_item.delete()

    return redirect('/viewcart')

@login_required(login_url='/admin/login/')
def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    cart_info = []
    full_total = 0

    for item in cart_items:
        subtotal = item.product.price * item.quantity
        full_total += subtotal

        cart_info.append({
            'product': item.product,
            'quantity': item.quantity,
            'subtotal': subtotal,
        })

    return render(request, 'cartItems.html', {'cart_items': cart_info})


def about_us_template(request):  
    return render(request, 'about_us.html')

def categories_template(request):  
    products = models.Product.objects.all()
    return render(request,'categories.html',{'products': products})


def home(request):
     products = models.Product.objects.all()
     return render(request, 'products.html',{'products': products})