from django.shortcuts import render
from .models import (
    Post,
    National,
    International,
    Politics,
    Literature,
    Trending,
    Blog,
    Sports,
    Entertainment,
    Covid,
    LifeStyle,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


class PostListView(ListView):
    model = Post
    template_name = "news/news.html"
    ordering = ["-timestamp"]
    context_object_name = "posts"


class PostDetailView(DetailView):
    model = Post


from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        "title",
        "post_owner",
        "image_owner",
        "address_month_day",
        "author",
        "text",
        "photo_1",
        "photo_2",
        "photo_3",
        "video",
        "yt_video",
    ]
    email = EmailMessage(
        "Thank You For Subscription",
        "Body",
        settings.EMAIL_HOST_USER,
        ["karkinirajan1999@gmail.com"],
    )
    email.fail_silently = True
    email.send()

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "text"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def national(request):
    context = {"posts": National.objects.all()}
    return render(request, "news/national.html", context)


# Class BASED VIEWS END HERE
def politics(request):
    context = {"posts": Politics.objects.all()}
    return render(request, "news/politics.html", context)


def sports(request):
    context = {"posts": Sports.objects.all()}
    return render(request, "news/sports.html", context)


def covid(request):
    context = {"posts": Covid.objects.all()}
    return render(request, "news/covid.html", context)


def international(request):
    context = {"posts": International.objects.all()}
    return render(request, "news/international.html", context)


def entertainment(request):
    context = {"posts": Entertainment.objects.all()}
    return render(request, "news/entertainment.html", context)


def lifestyle(request):
    context = {"posts": LifeStyle.objects.all()}
    return render(request, "news/lifestyle.html", context)


def blog(request):
    context = {"posts": Blog.objects.all()}
    return render(request, "news/blog.html", context)


def literature(request):
    context = {"posts": Literature.objects.all()}
    return render(request, "news/literature.html", context)


def trending(request):
    context = {"posts": Trending.objects.all()}
    return render(request, "news/trending.html", context)

