from django.contrib import admin
from .models import Blog, Category, Tags, Post
# Register your models here.
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Post)