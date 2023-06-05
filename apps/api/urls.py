from django.urls import path, include
from .views import ReviewAV, ProductVS
from django.utils.translation import gettext_lazy as _
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('productvs', ProductVS, basename='productvs')

urlpatterns = [
    path('proser/', ReviewAV.as_view(), name='proser'),
    path('', include(router.urls)),
]