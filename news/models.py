from django.db import models
from datetime import datetime
from django.urls import reverse
from embed_video.fields import EmbedVideoField
from django.utils import timezone
from django.contrib.auth.models import User

# from users.models import Profile
class Post(models.Model):
    title = models.CharField(max_length=200)
    post_owner = models.CharField(max_length=200)
    image_owner = models.ImageField(upload_to="media", blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    address_month_day = models.CharField(max_length=200)
    photo_0 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_1 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_2 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    photo_3 = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    video = models.FileField(upload_to="videos/%Y/%m/%d/", blank=True)
    yt_video = EmbedVideoField(max_length=140, blank=True)
    text = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})


class National(Post):
    pass


class International(Post):
    pass


class Politics(Post):
    pass


class Entertainment(Post):
    pass


class Covid(Post):
    pass


class Sports(Post):
    pass


class LifeStyle(Post):
    pass


class Trending(Post):
    pass


class Blog(Post):
    pass


class Literature(Post):
    pass
