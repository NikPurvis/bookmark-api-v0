# main_app/views.py

# Import dependencies
from django import http
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Import models
from .models import Book


# Views (like routes) created below.
# They're functions that are called by main_app's urls.py file.
# Those urls are registered in the project's (bookmark) urls.py.

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
    books = Book.objects.all().order_by("title")
    return render(request, "books/index.html", { "books": books })

# Books detail view
# Get an ID from the route parameter, defined in the url
def books_show(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "books/show.html", { "book": book })

# Bookclub view
def bookclub(request):
    return HttpResponse("<h1>Bookclub page!</h1>")

# Search view
def search(request):
    return HttpResponse("<h1>Search page!</h1>")

# Book community view
# def book_comm(request):
#     return HttpResponse("<h1>Book community page!</h1>")


# Defining a class to create books using Django's built-in methods
class BookCreate(CreateView):
    # Bases the form on the books model
    model = Book
    # Include all the fields on the form
    fields = "__all__"
    
    # It's not stricly necessary to call this method, but if we want to redirect to the details view page, we need to use this to get its primary key
    def form_valid(self, form):
        # Create an object from the form
        self.object = form.save(commit=False)
        # Save the object to the database
        self.object.save()
        # Redirect to its new detail page
        return HttpResponseRedirect("/cats" + str(self.object.pk))


class BookUpdate(UpdateView):
    model = Book
    fields = "__all__"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect("/cats" + str(self.object.pk))


class BookDelete(DeleteView):
    model = Book
    success_url = "/books"
