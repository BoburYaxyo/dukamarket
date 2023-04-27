from django.shortcuts import render
from shopping.models import Product
from shopping.utils import cartview
# Create your views here.


def home(request):
    product=Product.objects.all()
    myctx = cartview(request)
    context = {
        **myctx,
        'product': product
    }

    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def faq(request):
    return render(request, 'faq.html')


def contact(request):
    return render(request, 'contact.html')