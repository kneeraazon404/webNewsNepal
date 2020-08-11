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


class Blog(Post):
    pass


class Literature(Post):
    pass


class Tech(Post):
    pass


class Health(Post):
    pass


class Education(Post):
    pass


class Business(Post):
    pass


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)
    user_id = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    name = models.CharField(max_length=100, default=None)
    email = models.EmailField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


def get_comment(post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post).order_by("-id")[:5]
    return comments


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)


def if_liked(request, id):
    is_liked = Like.objects.filter(post=id).filter(user=request.user)
    if is_liked:
        return True
    else:
        return False
