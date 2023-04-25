from django.urls import path
from . import views
from shopping import views as viewvs

urlpatterns = [
    path('', viewvs.shop, name='product-details'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('product/<str:pk>/', views.single_prooduct, name="product"),
]
