from django.shortcuts import render, redirect, get_object_or_404
from shopping.models import Product, Review, Categories
# from shopping.forms import ReviewForm
# Create your views here.
from django.contrib.auth.decorators import login_required
from shopping.utils import cartview, wishview
from django.contrib import messages
from .models import Wishist


def single_prooduct(request, pk):
    # productObj = Product.objects.get(id=pk)
    product = get_object_or_404(Product, id=pk)
    # review = request.product.reviews.all()
    # form = ReviewForm
    category = Categories.objects.all()
    if request.method == 'POST':
        rating = request.POST.get('rating', 3)
        content = request.POST.get('content', '')
        
        if content:
            reviews = Review.objects.filter(created_by=request.user, product=product)
            if reviews.count() > 2:
                review = reviews.first()
                review.rating=rating
                review.content=content
                review.save()
            else:
                review = Review.objects.create(
                    product=product,
                    rating=rating,
                    content=content,
                    created_by = request.user
                )
            
            return redirect('product', pk=pk)
    myctx = cartview(request)
    qyctx = wishview(request)
    context = {
        **myctx,
        **qyctx,
        'product': product,
        'category': category
        }
    return render(request, 'product-details.html', context)


def wishlist(request):
    myctx = cartview(request)
    qyctx = wishview(request)
    category = Categories.objects.all()
    context = {
        **myctx,
        **qyctx,
        'category': category
    }
    return render(request, 'wishlist.html', context)


def wishList(request):
    dbctx: dict = {}
    dbctx["cartitems"] = 0

    if request.user.is_authenticated:
        wishProduct: Wishist = Wishist.objects.filter(
            user=request.user).prefetch_related("products").first()

        if wishProduct:
            dbctx["items"] = wishProduct.products.all()
            dbctx["wishProductsCount"] = wishProduct.products.count()

    return dbctx
