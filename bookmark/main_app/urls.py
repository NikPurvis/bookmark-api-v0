# main_app/urls.py

# Import dependencies
from django.urls import path
from . import views

# Mapping the views to URLs
urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("bookshelf/", views.bookshelf, name="bookshelf"),
    path("books/", views.books_index, name="books_index"),
    path("books/<int:book_id>/", views.books_show, name="books_show"),
    path("books/create/", views.BookCreate.as_view(), name="book_create"),
    path("book/<int:pk>/update/", views.BookUpdate.as_view(), name="book_update"),
    path("book/<int:pk>/delete/", views.BookDelete.as_view(), name="book_delete"),
    path("bookclub/", views.bookclub, name="bookclub"),
    path("search/", views.search, name="search")
]
