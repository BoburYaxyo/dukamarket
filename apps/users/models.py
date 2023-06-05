from django.db import models
from django.contrib.auth.models import User
import uuid

from django.urls import reverse
from shopping.models import Categories, Product
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
from currencies.models import Currency


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    profile_image = models.ImageField(
        null=True, blank=True, upload_to='images/', default="images/user-default.png")
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    birthday = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    @property 
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url

    def __str__(self):
        return str(self.username)


class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject
