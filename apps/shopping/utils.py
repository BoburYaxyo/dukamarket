import json
from .models import *
from django.db.models import Sum
from products.models import Cart, Wishlist



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
        wishProducts: Wishlist = Wishlist.objects.filter(
            user=request.user).prefetch_related("products").first()

        if wishProducts:
            qyctx["wishItems"] = wishProducts.products.all()
            qyctx["wishProductsCount"] = wishProducts.products.count()
            
            
    return qyctx