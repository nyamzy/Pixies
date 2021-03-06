from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField


# Create your models here.
class Profile(models.Model):
    profile_pic = models.ImageField(upload_to = 'images/')
    bio = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.bio

    # Save profile method
    def save_profile(self):
        self.save()

    # Delete profile method
    def delete_profile(self):
        self.delete()  

    # Update profile method
    def update_profile(self):
        updated_profile = Profile.objects.filter().update()
        return updated_profile


class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length=30)
    image_caption = HTMLField()
    pub_date = models.DateTimeField(auto_now_add = True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    # like_count = models.ManyToManyField(User, default = 0, related_name='liked')
    # comment_count = models.IntegerField(default = 0)
    # profile = models.ForeignKey(User, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.image_name

    # Save post method
    def save_post(self):
        self.save()

    # Delete post method
    def delete_post(self):
        self.delete()  

    # Update caption method
    def update_post(self):
        updated_post = Image.objects.filter().update()
        return updated_post

    # Search method
    @classmethod
    def search_image(cls, search_term):
        images = cls.objects.filter(image_name__icontains = search_term)
        return images

class Like(models.Model):
    LIKE_CHOICES = [
        ('Like', 'Like'),
        ('Unlike', 'Unlike'),
    ]

    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like', max_length=10)

    def str(self):
        return self.value


class Comment(models.Model):
    comment = models.CharField(max_length = 200)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    @classmethod
    def display_comment(cls,image_id):
        comments = cls.objects.filter(image_id = image_id)
        return comments