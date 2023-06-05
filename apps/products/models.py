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


class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    order_by = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=150)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    home_place_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    total_order = models.IntegerField(default=0)
    town_or_city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    post_code = models.CharField(max_length=100)
    email_adress = models.EmailField(max_length=100)
    ship_different = models.BooleanField(default=False)
    order_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name