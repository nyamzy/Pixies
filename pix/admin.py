from django.contrib import admin
from .models import Image, Profile, Comment, Like

# Register your models here.
admin.site.register(Image)
admin.site.register(Like)
admin.site.register(Profile)
admin.site.register(Comment)