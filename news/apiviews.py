from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse

from .models import *
from .models import *


def like(request, id):
    if request.is_ajax:
        if request.method == "POST":
            post = Post.objects.get(id=id)
            like = Like.objects.filter(post=post).filter(user=request.user)
            if like:
                like.delete()
                count = Like.objects.filter(post=post).count()
                truth = "True"
                is_liked = "Like"
            else:
                like = Like()
                like.user = request.user
                like.post = post
                like.like = True
                like.save()
                count = Like.objects.filter(post=post).count()
                truth = "False"
                is_liked = "Liked"
            return JsonResponse({"count": count, "truth": truth, "is_liked": is_liked})


def comment(request, id):
    if request.method == "POST":
        comment = request.POST["comment"]
        new_cmt = Comment()
        new_cmt.body = comment
        new_cmt.user = request.user
        new_cmt.post = Post.objects.get(id=id)
        if comment:
            new_cmt.save()
            data = {
                "comment": comment,
                "user": request.user.first_name + " " + request.user.last_name,
                "profile_picture": request.user.profile.profile_picture.url,
            }
            return JsonResponse(data)


def getlike(request, id):
    likers = []
    story = Post.objects.get(id=id)
    story.like = Like.objects.filter(post=story)
    for like in story.like:
        likers += User.objects.filter(id=like.user.id)
    return render(request, "shared/likers.html", {"likers": likers})

