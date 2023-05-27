from django.shortcuts import render
from shopping.models import Product, Categories
from shopping.utils import cartview, wishview
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    product=Product.objects.all()
    category = Categories.objects.all()
    myctx = cartview(request)
    qyctx = wishview(request)
    context = {
        **myctx,
        **qyctx,
        'product': product,
        'category': category
    }

    return render(request, 'home.html', context)


def about(request):
    category = Categories.objects.all()
    context = {'category':category}
    return render(request, 'about.html', context)


def faq(request):
    category = Categories.objects.all()
    context = {'category':category}
    return render(request, 'faq.html', context)

@login_required(login_url='login')
def contact(request):
    category = Categories.objects.all()
    context = {'category':category}
    return render(request, 'contact.html', context)