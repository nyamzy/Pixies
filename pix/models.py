from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict


# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.bio


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=30)
    caption = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add = True)
    profile = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    likes = models.ManyToManyField(User, related_name = 'liked', default = 0, null=True)
    comments = models.IntegerField(default = 0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = image, null = True)

    def __str__(self):
        return self.image_name


class Like(models.Model):
    LIKE_CHOICES = {
        ('Like', 'Like'),
        ('Unlike', 'Unlike'),
    }

    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='like', max_length=10)


class Comment(models.Model):
    comment = models.CharField(max_length = 200)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'comments')