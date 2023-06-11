from blog.models import Blog, Post
from products.models import Cart, Order
from shopping.models import Product, Review
# from rest_framework.response import Response
# from rest_framework import status\
from rest_framework import viewsets

from users.models import Profile
# from rest_framework.views import APIView
from .serializers import BlogSerializer, CartSerializer, OrderSerializer, PostSerializer, ProductSerializer, ProfileSerializer, ReviewSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework import generics, mixins

class ReviewVS(viewsets.ModelViewSet):

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

class CartVS(viewsets.ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()

class ProductVS(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProfileVS(viewsets.ModelViewSet):
    
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

class OrderVS(viewsets.ModelViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()


class BlogVS(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    
class PostVS(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()

