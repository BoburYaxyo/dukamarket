from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from users.models import Profile
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    bcategory = models.ForeignKey(Category, on_delete=models.CASCADE)
    popular_feed = models.BooleanField(default=False)
    btag = models.ManyToManyField(Tags)
    posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = RichTextUploadingField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Post(models.Model):
    blog = models.ForeignKey(
        Blog, related_name="posts", on_delete=models.CASCADE)
    comment = models.TextField()
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    website = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User, related_name="posts", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
