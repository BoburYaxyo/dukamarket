from django.shortcuts import render
from shopping.models import Product, Review
from shopping.forms import ReviewForm
# Create your views here.
from django.contrib import messages

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
    return render(request, 'wishlist.html')

