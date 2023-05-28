from django.utils import translation
from django.utils.translation import gettext_lazy as _
from django.http import HttpResponseRedirect
from django.shortcuts import render
from dukamarket import settings
from shopping.models import Product, Categories
from shopping.utils import cartview, wishview
from django.contrib.auth.decorators import login_required
from currencies.models import Currency
from users.models import Profile
from django.utils.translation import gettext as _
@login_required(login_url='login')
def home(request):
    product=Product.objects.all()
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


def selectcurrency(request):
    lasturl = request.META.get('HTTP_REFERER')
    if request.method == 'POST': # check post
        request.session['currency'] = request.POST['currency']
    return HttpResponseRedirect(lasturl)

def selectlanguage(request):
    if request.method == 'POST': # check post
        cur_language = translation.get_language()
        lasturl=request.META.get('HTTP_REFERER')
        lang = request.POST['language']
        translation.activate(lang)
        request.session[translation.LANGUAGE_SESSION_KEY]=lang
        return HttpResponseRedirect("/"+lang)
@login_required(login_url='/login')
def savelangcur(request):
    lasturl = request.META.get('HTTP_REFERER')
    curren_user = request.user
    language = Language.objects.get(code=request.LANGUAGE_CODE[0:2])
    #save to user profile database
    data = Profile.oobjects.get(user_id=curren_user.id)
    data.language_id = language.id
    data.currency_id = request.session['currency']
    data.save()
    return HttpResponseRedirect(lasturl)