from django.shortcuts import render
from shopping.models import Product
from shopping.utils import cartview, wishview
from django.contrib.auth.decorators import login_required


 
@login_required(login_url='login')
def home(request):
    product=Product.objects.all()
    myctx = cartview(request)
    qyctx = wishview(request)
    context = {
        **myctx,
        **qyctx,
        'product': product
    }

    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def faq(request):
    return render(request, 'faq.html')

@login_required(login_url='login')
def contact(request):
    return render(request, 'contact.html')