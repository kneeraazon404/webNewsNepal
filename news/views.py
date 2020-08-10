from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import (
    Post,
    National,
    International,
    Politics,
    Literature,
    Blog,
    Sports,
    Entertainment,
    Covid,
    LifeStyle,
    Tech,
    Health,
    Education,
    Business,
    Contact,
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
    template_name = "news/home.html"
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
    # email.send()

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


def business(request):
    context = {"posts": Business.objects.all()}
    return render(request, "news/business.html", context)


def education(request):
    context = {"posts": Education.objects.all()}
    return render(request, "news/education.html", context)


def health(request):
    context = {"posts": Health.objects.all()}
    return render(request, "news/health.html", context)


def tech(request):
    context = {"posts": Tech.objects.all()}
    return render(request, "news/tech.html", context)


@login_required
def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        message = request.POST["message"]
        user_id = request.POST.get("user_id")

        # Check if user has contacted already
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already sent us a message")
                return redirect("/news/contact.html")

        contact = Contact(
            name=name, email=email, phone=phone, message=message, user_id=user_id,
        )

        contact.save()

        messages.success(
            request, "Your message has been sent, We will get back to you soon",
        )

        return redirect("/")

    return render(request, "news/contact.html")
