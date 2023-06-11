from django.urls import path, include
from .views import BlogVS, CartVS, PostVS, ProfileVS, ReviewVS, ProductVS, OrderVS
from django.utils.translation import gettext_lazy as _
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('productvs', ProductVS, basename='productvs')
router.register('ordervs', OrderVS, basename='ordervs')
router.register('blogvs', BlogVS, basename='blogvs')
router.register('postvs', PostVS, basename='postvs')
router.register('reviewvs', ReviewVS, basename='reviewvs')
router.register('cartvs', CartVS, basename='cartvs')
router.register('profilevs', ProfileVS, basename='profilevs')


urlpatterns = [
    path('', include(router.urls)),
]
