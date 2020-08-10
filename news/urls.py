from django.urls import path
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

urlpatterns = [
    path("", PostListView.as_view(), name="home"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("national/", views.national, name="national"),
    path("covid/", views.covid, name="covid"),
    path("politics/", views.politics, name="politics"),
    path("international/", views.international, name="international"),
    path("sports/", views.sports, name="sports"),
    path("entertainment/", views.entertainment, name="entertainment"),
    path("lifestyle/", views.lifestyle, name="lifestyle"),
    path("blog/", views.blog, name="blog"),
    path("literature/", views.literature, name="literature"),
    path("trending/", views.health, name="health"),
    path("trending/", views.education, name="education"),
    path("trending/", views.business, name="business"),
    path("trending/", views.tech, name="tech"),
]

