from django.contrib import admin

from .models import PostImage, Post, LikedPost, Comment, LikedComment

admin.site.register([PostImage, Post, LikedPost, Comment, LikedComment])
