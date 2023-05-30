from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('blog-details/<int:pk>/', views.blog_details, name='blog-details'),
]
