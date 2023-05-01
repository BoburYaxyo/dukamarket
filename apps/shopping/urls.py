from django.urls import path
from . import views


urlpatterns = [
    path('', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    

    path('add_cart/<str:id>/', views.addCartView, name="add-cart"),
    path('add_cart/<str:id>/', views.addWishlistView, name="add-wish"),
]
