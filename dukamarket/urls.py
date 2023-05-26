from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from django.views.static import serve

urlpatterns = [
    path('', include('home.urls')),

    path('users/', include('users.urls')),

    path('blog/', include('blog.urls')),

    path('shopping/', include('shopping.urls')),

    path('products/', include('products.urls')),

    path('admin/', admin.site.urls),
    
    path('api/', include('api.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
