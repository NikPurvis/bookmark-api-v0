# main_app/urls.py

# Import dependencies
from django.urls import path
from . import views

# Mapping the views to URLs
urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("bookshelf/", views.bookshelf, name="bookshelf"),
    path("book/", views.book, name="book"),
    path("bookclub/", views.bookclub, name="bookclub"),
    path("search/", views.search, name="search")
]