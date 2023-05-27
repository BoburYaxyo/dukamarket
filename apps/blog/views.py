from django.shortcuts import render
from shopping.models import Categories
# Create your views here.


def blog(request):
    category = Categories.objects.all()
    context = {'category':category}
    return render(request, 'blog.html')


def blog_details(request):
    category = Categories.objects.all()
    context = {'category':category}
    return render(request, 'blog-details.html')