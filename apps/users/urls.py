from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logoutUser, name='logout'),
    path('checkout/', views.checkout, name='checkout'),
    path('404/', views.errorim, name='404'),
    path('', views.profile, name='admin-page'),
    path('user-page/', views.userprofile, name='profile'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name="password_reset_form.html"), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name="password_reset_done.html"), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name="password_reset_complete.html"), name='password_reset_complete'),
]
