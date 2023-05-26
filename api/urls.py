from django.urls import path
from .views import ProductAV

urlpatterns = [
    path('proser/', ProductAV.as_view(), name='proser')
]