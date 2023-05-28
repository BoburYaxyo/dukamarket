import django.conf.urls.i18n
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from django.views.static import serve
from django.utils.translation import gettext_lazy as _
from home import views

urlpatterns = [
    path('selectlanguage', views.selectlanguage, name='selectlanguage'),
    path('selectcurrency', views.selectcurrency, name='selectcurrency'),
    path('savelangcur', views.savelangcur, name='savelangcur'),
    path('i18n/', include(django.conf.urls.i18n)),
]  

urlpatterns += i18n_patterns(
    path('', include('home.urls')),

    path('users/', include('users.urls')),

    path(_('blog/'), include('blog.urls')),

    path('shopping/', include('shopping.urls')),
    path('products/', include('products.urls')),
    path('currencies/', include('currencies.urls')),
    path(_('admin/'), admin.site.urls),
    
    path('api/', include('api.urls')),
    # path('ckeditor/', include('ckeditor_uploader.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
