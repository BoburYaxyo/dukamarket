from django.shortcuts import redirect, render
from shopping.models import Categories
from shopping.utils import cartview, wishview
from .models import Category, Blog, Post
from django.db.models import Q
from blog.utils import paginateBlogs
# Create your views here.


def blog(request):
    category = Categories.objects.all()
    bcategory = Category.objects.all()
    b = request.GET.get('b') if request.GET.get('b') != None else ''
    blogs = Blog.objects.filter(
        Q(name__icontains=b) |
        Q(bcategory__name__icontains=b) |
        Q(title__icontains=b)
    )
    custom_range, blogs = paginateBlogs(request, blogs, 2)
    myctx = cartview(request)
    qyctx = wishview(request)
    context = {
        **myctx,
        **qyctx,
        'category': category,
        'bcategory': bcategory,
        'blogs': blogs,
        'custom_range': custom_range,
    }
    return render(request, 'blog.html', context)


def blog_details(request, pk):
    blog = Blog.objects.get(pk=pk)
    if request.method == 'POST':
        name = request.POST.get('name', '')
        comment = request.POST.get('comment', '')
        email = request.POST.get('email', '')
        website = request.POST.get('website', '')

        if comment:
            posts = Post.objects.filter(created_by=request.user, blog=blog)
            if posts.count() > 2:
                post = posts.first()
                post.comment = comment
                post.name = name
                post.email = email
                post.website = website
                post.save()
            else:
                post = Post.objects.create(
                    blog=blog,
                    name=name,
                    comment=comment,
                    email=email,
                    website=website,
                    created_by=request.user,
                )

            return redirect('blog-details', pk=pk)
    bcategory = Category.objects.all()
    b = request.GET.get('b') if request.GET.get('b') != None else ''
    blogs = Blog.objects.filter(
        Q(name__icontains=b) |
        Q(bcategory__name__icontains=b) |
        Q(title__icontains=b)
    )
    category = Categories.objects.all()
    myctx = cartview(request)
    qyctx = wishview(request)
    context = {
        **myctx,
        **qyctx,
        'category': category,
        'blog': blog,
        'bcategory': bcategory,
        'blogs': blogs
    }
    return render(request, 'blog-details.html', context)
