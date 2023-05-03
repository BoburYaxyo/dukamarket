from django.shortcuts import render, redirect

from shopping.utils import cartview, wishview
# Create your views here.
from products.models import Cart, Wishist
from .forms import ReviewForm
from django.http import JsonResponse
import json
import datetime
from .models import *
from products.forms import CartForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def addCartView(request, id) -> None:

    product: Product = Product.objects.get(id=id)
    cart, _ = Cart.objects.get_or_create(user=request.user)
    cart.products.add(product)
    cart.save()

    return redirect('home')


@login_required(login_url='login')
def addWishlistView(request, id) -> None:

    product: Product = Product.objects.get(id=id)
    wishlist, _ = Wishist.objects.get_or_create(user=request.user)
    wishlist.products.add(product)
    wishlist.save()

    return redirect('shop')


@login_required(login_url='login')
def shop(request):

    products = Product.objects.all()
    myctx = cartview(request)
    qyctx = wishview(request)
    context = {
        **myctx,
        **qyctx,
        'products': products
    }
    return render(request, 'shop.html', context)


@login_required(login_url='login')
def cart(request):
    myctx = cartview(request)

    context = {**myctx, }
    return render(request, 'cart.html', context)
