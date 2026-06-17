from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from . models import profile_table
from django.contrib import messages
from .models import products,Cart,CartItem,Wishlist,WishlistItem,ordered_pro

# Create your views here.
def login_user(request):
    if request.method == "POST":
       n=request.POST.get('inp_name')
       a=request.POST.get('inp_email')
       b=request.POST.get('inp_pass')
       c=authenticate(username=n,password=b)
       if c:
           login(request,c)
           return redirect('home')
       else:
           messages.warning(request,"Invalid User!Please register to continue.")
           return redirect('login_user')
    return render(request,'login.html')

def register_user(request):
    if request.method == "POST":
       n=request.POST.get('reg_name')
       a=request.POST.get('reg_email')
       b=request.POST.get('reg_pass')
       user=User.objects.create_user(username=n,email=a,password=b)
       c=request.POST.get('reg_address')
       d=request.POST.get('reg_num')
       profile_table.objects.create(user=user,address=c,contact_number=d)
       return redirect('login_user')
    return render(request,'register.html')

def profile(request):
    profile=profile_table.objects.get(user=request.user)
    context={'user':request.user , 'profile_table':profile}
    return render(request,'profile.html',context)

def edit_profile(request):
    profile = profile_table.objects.get(user=request.user)
    user = request.user

    if request.method == "POST":
        user.username = request.POST.get('edit_name')
        user.email = request.POST.get('edit_email')

        profile.address = request.POST.get('edit_address')
        profile.contact_number = request.POST.get('edit_num')

        user.save()
        profile.save()

        return redirect('profile')

    context = {
        'user': user,
        'profile_table': profile
        }

    return render(request, 'edit_profile.html', context)

def home(request):
    product = products.objects.all()
    cart_count = 0
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_count = CartItem.objects.filter(cart=cart).count()

    context = {'product': product,'cart_count': cart_count}
    return render(request, 'home.html', context)
    
def add_to_cart(request, id):
    product = products.objects.get(id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )
    if not created:
        item.quantity += 1
        item.save()
    return redirect('home')

def cart(request):
    cart = Cart.objects.get(user=request.user)
    items = CartItem.objects.filter(cart=cart)
    context = {
        'items': items
    }
    return render(request, 'cart.html', context)

def add_to_wishlist(request, id):
    product = products.objects.get(id=id)
    wishlist, created = Wishlist.objects.get_or_create(
        user=request.user
    )
    WishlistItem.objects.get_or_create(
        wishlist=wishlist,
        product=product
    )
    return redirect('home')
def wishlist(request):
    wishlist = Wishlist.objects.get(user=request.user)
    items = WishlistItem.objects.filter(wishlist=wishlist)
    context = {
        'items': items
    }
    return render(request, 'wishlist.html', context)
def delete_c(request,id):
    a=CartItem.objects.get(id=id)
    a.delete()
    return redirect('cart')
def delete_w(request,id):
    a=WishlistItem.objects.get(id=id)
    a.delete()
    return redirect('wishlist')
def increase_quantity(request, id):
    item = CartItem.objects.get(id=id)
    item.quantity += 1
    item.save()
    return redirect('cart')
def decrease_quantity(request, id):
    cart_item = CartItem.objects.get(id=id)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()     
    return redirect('cart')
def order_confirm(request):
    cart = Cart.objects.get(user=request.user)
    a= CartItem.objects.filter(cart=cart)
    for i in a:
        ordered_pro.objects.create(user=request.user,product=i.product,quantity=i.quantity)
    a.delete()
    return render(request,'order.html')

def recent_orders(request):
    a=ordered_pro.objects.filter(user=request.user)
    return render(request,'recent.html',{'a':a})



