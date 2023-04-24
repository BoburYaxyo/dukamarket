from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Review(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=150)
    review=models.TextField()
    
    def __str__(self):
        return self.name

class Product_category(models.Model):
    name=models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name=models.CharField(max_length=150)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product_image=models.ImageField(null=True, blank=True, upload_to='images/', default='/images/default.jpg')
    price = models.DecimalField(
        max_digits=1000, decimal_places=1, default=0, blank=True, null=True)
    overall_rating = models.DecimalField(max_digits=1000, decimal_places=1, default=0, blank=True, null=True)
    category=models.ForeignKey(Product_category, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
            return url




