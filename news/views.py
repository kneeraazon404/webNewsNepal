from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from .forms import subForm
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import subForm
from .models import (
    Blog,
    Business,
    Contact,
    Covid,
    Education,
    Entertainment,
    Health,
    International,
    LifeStyle,
    Literature,
    National,
    Politics,
    Post,
    Sports,
    Tech,
)


class PostListView(ListView):
    model = Post
    template_name = "news/home.html"
    context_object_name = "posts"
    ordering = ["-timestamp"]
    paginate_by = 6


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = "__all__"
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
    context = {"nationals": National.objects.all()}
    return render(request, "news/national.html", context)


# Class BASED VIEWS END HERE
def politics(request):
    context = {"politics": Politics.objects.all()}
    return render(request, "news/politics.html", context)


class SportListView(PostListView):
    model = Sports
    template_name = "news/sports.html"
    context_object_name = "sports"
    ordering = ["-timestamp"]
    paginate_by = 6


def covid(request):
    context = {"covids": Covid.objects.all()}
    return render(request, "news/covid.html", context)


def international(request):
    context = {"posts": International.objects.all()}
    return render(request, "news/international.html", context)


def entertainment(request):
    context = {"entertainments": Entertainment.objects.all()}
    return render(request, "news/entertainment.html", context)


def lifestyle(request):
    context = {"lifestyles": LifeStyle.objects.all()}
    return render(request, "news/lifestyle.html", context)


def blog(request):
    context = {"blogs": Blog.objects.all()}
    return render(request, "news/blog.html", context)


def literature(request):
    context = {"literatures": Literature.objects.all()}
    return render(request, "news/literature.html", context)


def business(request):
    context = {"business": Business.objects.all()}
    return render(request, "news/business.html", context)


def education(request):
    context = {"educations": Education.objects.all()}
    return render(request, "news/education.html", context)


def health(request):
    context = {"healths": Health.objects.all()}
    return render(request, "news/health.html", context)


def tech(request):
    context = {"techs": Tech.objects.all()}
    return render(request, "news/tech.html", context)


@login_required()
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

        contact = Contact(
            name=name, email=email, phone=phone, message=message, user_id=user_id,
        )

        contact.save()

        messages.success(
            request, "Your message has been sent, We will get back to you soon",
        )

        return redirect("/")

    return render(request, "contact/contact.html")


def subscribe(request):
    subs = subForm()
    context = {"subs": subs}
    if request.method == "POST":
        subs = subForm(request.POST, request.FILES)
        if subs.is_valid():
            subs.save()
            messages.success(request, "Thank You for Subscription")
        return redirect("home")
    return render(request, "news/home.html", context)
