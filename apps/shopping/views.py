from django.shortcuts import render, redirect

from shopping.utils import cartview, wishview
# Create your views here.
from products.models import Cart, Wishist, Product
# from .forms import ReviewForm
from django.http import JsonResponse
import json
import datetime
from .models import *
from django.contrib import messages
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
        'products': products,

    }
    return render(request, 'shop.html', context)


@login_required(login_url='login')
def cart(request):
    myctx = cartview(request)

    context = {**myctx, }
    return render(request, 'cart.html', context)

@login_required(login_url='login')
def removeWishlistView(request, id: int) -> None:
    wishProducts: Wishist = Wishist.objects.filter(
        user=request.user).prefetch_related("products").first()
    if wishProducts:
        wishItem = wishProducts.products.get(id=id)
        wishProducts.products.remove(wishItem)

    return redirect('wishlist')


@login_required(login_url='login')
def removeCartView(request, id: int) -> None:
    cartProducts: Cart = Cart.objects.filter(
        user=request.user).prefetch_related("products").first()
    if cartProducts:
        cartItem = cartProducts.products.get(id=id)
        cartProducts.products.remove(cartItem)
        messages.add_message(request, messages.INFO,
                             'Savatchadan muvaffaqqiyatli o\'chirildi ✅')

    return redirect('cart')