from django.shortcuts import render
from shopping.models import Product

# Create your views here.


def single_prooduct(request, pk):
    productObj = Product.objects.get(id=pk)

    context = {'product': productObj}
    return render(request, 'product-details.html', context)


def wishlist(request):
    return render(request, 'wishlist.html')
