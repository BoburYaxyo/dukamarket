from django.utils import translation
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect
from django.shortcuts import render
from blog.models import Blog
from dukamarket import settings
from shopping.models import Product, Categories
from shopping.utils import cartview, wishview
from django.contrib.auth.decorators import login_required
from currencies.models import Currency
from users.models import Profile
from django.utils.translation import gettext as _


@login_required(login_url='login')
def home(request):
    blogs = Blog.objects.all()
    product = Product.objects.all()
    category = Categories.objects.all()
    defaultcurr = settings.DEFAULT_CURRENCY
    if not request.session.has_key('currency'):
        request.session['currency'] = settings.DEFAULT_CURRENCY
    myctx = cartview(request)
    qyctx = wishview(request)
    
    context = {
        **myctx,
        **qyctx,
        'hello': _('Hello'),
        'product': product[0:5],
        'dproduct': product[0:6],
        'category': category,
        'blogs': blogs
    }

    return render(request, 'home.html', context)


def about(request):
    page = 'about'
    category = Categories.objects.all()
    myctx = cartview(request)
    qyctx = wishview(request)
    
    context = {
        **myctx,
        **qyctx,
        'category': category,
        'page': page
        }
    return render(request, 'about.html', context)


def faq(request):
    page = 'faq'
    category = Categories.objects.all()
    myctx = cartview(request)
    qyctx = wishview(request)
    context = {
        **myctx,
        **qyctx,
        'category': category,
        'page': page
        }
    return render(request, 'faq.html', context)


@login_required(login_url='login')
def contact(request):
    page = 'contact'
    category = Categories.objects.all()
    myctx = cartview(request)
    qyctx = wishview(request)
    context = {
        **myctx,
        **qyctx,
        'category': category,
        'page': page
        }
    return render(request, 'contact.html', context)


def selectcurrency(request):
    lasturl = request.META.get('HTTP_REFERER')
    if request.method == 'POST':  # check post
        request.session['currency'] = request.POST['currency']
    return HttpResponseRedirect(lasturl)


def selectlanguaged(request):
    if request.method == 'POST':  # check post
        cur_language = translation.get_language()
        lasturl = request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY] = lang
        return HttpResponseRedirect("/"+lang+'/about')


def selectlanguager(request):
    if request.method == 'POST':  # check post
        cur_language = translation.get_language()
        lasturl = request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY] = lang
        return HttpResponseRedirect("/"+lang+'/faq')


def selectlanguage(request):
    if request.method == 'POST':  # check post
        cur_language = translation.get_language()
        lasturl = request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY] = lang
        return HttpResponseRedirect("/"+lang+'/contact')


@login_required(login_url='/login')
def savecur(request):
    lasturl = request.META.get('HTTP_REFERER')
    curren_user = request.user
    # save to user profile database
    data = Profile.objects.get(user_id=curren_user.id)
    data.currency_id = request.session['currency']
    data.save()
    return HttpResponseRedirect(lasturl)
