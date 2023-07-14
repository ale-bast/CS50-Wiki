from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("create/", views.create, name="create"),
    path("edit/<str:title>", views.edit, name="edit"),
    path("random/", views.random_page, name="random")
]
