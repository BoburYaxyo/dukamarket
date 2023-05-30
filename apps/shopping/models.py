from urllib import request
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Categories(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name




class Colors(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Brands(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Sizes(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    # reviews = models.ManyToManyField(Review, related_name='reviews')
    color = models.ForeignKey(Colors, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, null=True)
    size = models.ForeignKey(Sizes, on_delete=models.SET_NULL, null=True, blank=True)
    brands = models.ForeignKey(Brands, on_delete=models.SET_NULL, null=True, blank=True)
    sold = models.IntegerField(default=0)
    free = models.IntegerField(default=0)
    skills = models.TextField(null=True)
    special_offers = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name

    def get_rating(self):
        reviews_total = 0

        for review in self.reviews.all():
            reviews_total += int(review.rating)

        if reviews_total > 0:
            return reviews_total // self.reviews.count()

        return 0

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class Review(models.Model):
    product = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE)
    rating = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(
        User, related_name="reviews", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

