# main_app/views.py

# Import dependencies
from django import http
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout

# Import models
from .models import Book
# Import forms
from .forms import LoginForm


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
        return HttpResponseRedirect("/books/" + str(self.object.pk))


class BookUpdate(UpdateView):
    model = Book
    fields = "__all__"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect("/books/" + str(self.object.pk))


class BookDelete(DeleteView):
    model = Book
    success_url = "/books"


# login view
def login_view(request):
    # We can use the same view for multiple HTTP requests
    # This can be doen with a simple if statement
    if request.method == "POST":
        # handle post request
        # We want to authentic the user with the username and password
        form = LoginForm(request.POST)
        # Validate the form data
        if form.is_valid():
            # get the username and password and save them to variables
            u = form.cleaned_data["username"]
            p = form.cleaned_data["password"]
            # We use Django's built-in authenticate method
            user = authenticate(username = u, password = p)
            # If you found a user with matching credentials
            if user is not None:
                # If the user hasn't been disabled by admin
                if user.is_active:
                    # Use Django's built-in login function
                    login(request, user)
                    # return HttpResponseRedirect("/user/" + str(user.username))
                    return HttpResponseRedirect("/")
                else:
                    print("The account has been disabled.")
            else:
                print("The username or password is incorrect.")
    else:
        # The request is a GET, we render the login page
        form = LoginForm()
        return render(request, "auth/login.html", { "form": form })

# logout view
def logout_view(request):
    # print("##### THIS IS THE REQUEST ######")
    # print(request)
    # print(request.user)
    logout(request)
    return HttpResponseRedirect("/cats/")

# Signup view
def signup_view(request):
    # If the request is a POST, sign them up
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect("/user/" + str(user.username))
        
    # If the request is a GET, show the form.
    else:
        form = UserCreationForm()
        return render(request, "signup.html", { "form": form })
