from django.shortcuts import render

# Create your views here.


def product_details(request):
    return render(request, 'product-details.html')


def wishlist(request):
    return render(request, 'wishlist.html')