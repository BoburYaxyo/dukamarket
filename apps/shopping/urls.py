from django.urls import path
from . import views
from django.utils.translation import gettext as _


urlpatterns = [
    path('', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    

    path('add_cart/<str:id>/', views.addCartView, name="add-cart"),
    path('add_wish/<str:id>/', views.addWishlistView, name="add-wish"),
    path('remove_cart/<int:id>/', views.removeCartView, name="rem-cart"),
    path('remove_wish/<int:id>/', views.removeWishlistView, name="rem-wish"),
]
