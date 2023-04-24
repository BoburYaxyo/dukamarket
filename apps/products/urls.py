from django.urls import path
from . import views


urlpatterns = [
    path('', views.product_details, name='product-details'),
    path('wishlist/', views.wishlist, name='wishlist'),
]
