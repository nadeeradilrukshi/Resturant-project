from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem
from django.contrib.auth.decorators import login_required
from . import models
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.shortcuts import redirect


# ... (your other views)



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

    return render(request, 'cartItems.html', {'cart_items': cart_info, 'full_total': full_total})


def about_us_template(request):  
    return render(request, 'about_us.html')

def categories_template(request):  
     return render(request, 'categories.html')


def home1(request):
     return render(request, 'base.html')
 
def homepage(request):
     return render(request, 'homepage.html')
 
# def items(request):
#      return render(request, 'items.html')

# def items(request):  
#     products = models.Product.objects.all()
#     return render(request,'items.html',{'products': products})

def items(request):
    query = request.GET.get('q')
    if query:
        products = models.Product.objects.filter(Q(name_icontains=query) | Q(description_icontains=query))
    else:
        products = models.Product.objects.all()

    return render(request, 'items.html', {'products': products})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Change 'home' to the name of your home view
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


# views.py

def logout_view(request):
    logout(request)
    return redirect('login')  # Replace 'login' with the actual name or path of your login view

def checkout(request):
    return render(request, 'checkout.html')