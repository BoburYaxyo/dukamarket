from django.shortcuts import render
from shopping.models import Product, Review
from shopping.forms import ReviewForm
# Create your views here.
from shopping.utils import cartview, wishview
from django.contrib import messages
from .models import Wishlist
def single_prooduct(request, pk):
    productObj = Product.objects.get(id=pk)
    form = ReviewForm
    review=Review.objects.all()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            form.save()
        else:
            messages.success(
                request, 'An error has occurred during registration')   
    context = {'product': productObj, 'form': form, 'reviews': review}
    return render(request, 'product-details.html', context)


def wishlist(request):
    myctx = cartview(request)
    qyctx = wishview(request)
    context = {
        **myctx,
        **qyctx,
    }
    return render(request, 'wishlist.html', context)

def wishList(request):
    dbctx: dict = {}
    dbctx["cartitems"] = 0

    if request.user.is_authenticated:
        wishProduct: Wishlist = Wishlist.objects.filter(
            user=request.user).prefetch_related("products").first()

        if wishProduct:
            dbctx["items"] = wishProduct.products.all()
            dbctx["wishProductsCount"] = wishProduct.products.count()

    return dbctx 

