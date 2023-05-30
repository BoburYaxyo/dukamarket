from django.urls import path
from .views import ProductAV
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('proser/', ProductAV.as_view(), name='proser')
]