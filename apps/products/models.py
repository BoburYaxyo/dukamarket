from django.db import models
from django.contrib.auth.models import User
from shopping.models import Product


class Wishist(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.PROTECT)
    products = models.ManyToManyField(
        Product, blank=True, related_name='wishlistproducts')


class Cart(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.PROTECT)
    products = models.ManyToManyField(
        Product, blank=True, related_name='cartproducts')
