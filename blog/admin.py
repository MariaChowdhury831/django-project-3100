from django.contrib import admin
from .models import post

admin.site.register(post)
from django.contrib import admin
from blog.models import BlogComment

admin.site.register(BlogComment)