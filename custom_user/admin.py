# custom_user/admin.py
from django.contrib import admin
from .models import CustomUser, Profile, Post, Comment

admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
