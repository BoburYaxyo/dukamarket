from django.db import models
from django.contrib.auth.models import User
from shopping.models import Product, Shipping


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


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shipping = models.ForeignKey(Shipping, on_delete=models.CASCADE)
    order_by = models.ForeignKey(User, on_delete=models.CASCADE)
    order_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name