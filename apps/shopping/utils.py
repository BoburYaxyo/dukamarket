import json
from .models import *
from django.db.models import Sum
from products.models import Cart, Wishist
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def cartview(request) -> dict:
    myctx: dict = {}
    myctx["cart_count"] = 0

    if request.user.is_authenticated:
        cart_products = Cart.objects.filter(
            user=request.user).prefetch_related("products").first()

    if cart_products:
        myctx["sum_price"] = cart_products.products.aggregate(
            Sum('price')).get('price__sum')
        myctx['cartitems'] = cart_products.products.all()
        myctx['cart_count'] = cart_products.products.count()
    return myctx


def wishview(request):
    qyctx: dict = {}
    qyctx["wishProductsCount"] = 0

    if request.user.is_authenticated:
        wishProducts: Wishist = Wishist.objects.filter(
            user=request.user).prefetch_related("products").first()

        if wishProducts:
            qyctx["wishItems"] = wishProducts.products.all()
            qyctx["wishProductsCount"] = wishProducts.products.count()

    return qyctx


def paginateProducts(request, products, results):

    page = request.GET.get('page')
    paginator = Paginator(products, results)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        products = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        products = paginator.page(page)

    leftIndex = (int(page) - 4)

    if leftIndex < 1:
        leftIndex = 1

    rightIndex = (int(page) + 5)

    if rightIndex > paginator.num_pages:
        rightIndex = paginator.num_pages + 1

    custom_range = range(leftIndex, rightIndex)

    return custom_range, products
