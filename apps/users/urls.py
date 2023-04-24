from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.checkout, name='checkout'),
    path('404/', views.errorim, name='404'),
]
