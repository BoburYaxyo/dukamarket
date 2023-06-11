from django.db import models
from django.contrib.auth.models import User
# Create your models here.

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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    price = models.FloatField(null=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    color = models.ForeignKey(Colors, on_delete=models.CASCADE)
    tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(
        Categories, on_delete=models.SET_NULL, null=True)
    skills = models.CharField(max_length=200, null=True, blank=True)
    size = models.ManyToManyField(
        Sizes, blank=True)
    brands = models.ForeignKey(
        Brands, on_delete=models.SET_NULL, null=True, blank=True)
    free = models.IntegerField(default=0)
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
