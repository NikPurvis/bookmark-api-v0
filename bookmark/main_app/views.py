# main_app/views.py

# Import dependencies
from django import http
from django.shortcuts import render
from django.http import HttpResponse
# Import models
from .models import Book


# Index view
def index(request):
    return render(request, "index.html")

# Profile view
def profile(request):
    return HttpResponse("<h1>Profile page!</h1>")

# Bookshelf view
def bookshelf(request):
    return HttpResponse("<h1>Bookshelf page!</h1>")

# Book view
def books_index(request):
    books = Book.objects.all()
    return render(request, "books/index.html", { "books": books })

# Bookclub view
def bookclub(request):
    return HttpResponse("<h1>Bookclub page!</h1>")

# Search view
def search(request):
    return HttpResponse("<h1>Search page!</h1>")

# Book community view
# def book_comm(request):
#     return HttpResponse("<h1>Book community page!</h1>")
