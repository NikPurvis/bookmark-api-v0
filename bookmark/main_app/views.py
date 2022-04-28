# main_app/views.py

# Import dependencies
from django import http
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist

# Import models
from .models import Book, Bookshelf, Review
from django.contrib.auth.models import User
# Import forms
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm


# Views (like routes) created below.
# They're functions that are called by main_app's urls.py file.
# Those urls are registered in the project's (bookmark) urls.py.

##################
##  BASIC SITE
##################
#
# # Index view
# def index(request):
#     return render(request, "index.html")
def index(request):
    books = Book.objects.all()
    data = list(books.values())
    return JsonResponse(data)


# Profile view
def profile(request, username):
    user = User.objects.get(username=username)

    return render(request, "profile.html", { "username": username })

# Bookclub view
def bookclub(request):
    return HttpResponse("<h1>Bookclub page!</h1>")

# Search view
def search(request):
    return HttpResponse("<h1>Search page!</h1>")

# Book community view
# def book_comm(request):
#     return HttpResponse("<h1>Book community page!</h1>")



##################
##  BOOKS
##################
#
# Book view
def books_index(request):
    books = Book.objects.all().order_by("title")
    return render(request, "books/index.html", { "books": books })

# Books detail view
# Get an ID from the route parameter, defined in the url
def books_show(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "books/show.html", { "book": book })


# Defining classes to create forms using Django's built-in methods
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


##################
##  BOOKSHELF
##################
#
# Bookshelf view
def bookshelf(request, username):
    # Check to see if the user already has a bookshelf.
    # If yes, move on.
    try:
        user = User.objects.get(username=username)
        found_shelf = Bookshelf.objects.get(owner_id=user.id)
    # If no bookshelf object exists connected to the user...
    except Bookshelf.DoesNotExist:
        # ...create a new bookshelf object...
        new_shelf = Bookshelf.objects.create(
            owner_id=user.id)
        # ...save it...
        new_shelf.save()
        # ...and give the pertinent object info to the variable we're working with for the rest of the view.
        found_shelf = new_shelf

    # Filters books to just those found on the user's bookshelf.
    shelf_books = Book.objects.filter(id__in = found_shelf.shelved.all().values_list("id"))

    # Test stuff for seeing the SQL queries Django is running.
    # print("******************")
    # print(connection.queries)
    # print("******************")

    # Passes the filtered bookshelf to the template for display.
    return render(request, "bookshelf.html", {
        "username": username,
        "bookshelf": shelf_books })


# Bookshelf add view
def bookshelf_add(request, book_id):
    # Get the user id from the request info (session)
    user_id = request.user.id
    # Get the user's bookshelf
    user_shelf = Bookshelf.objects.get(owner_id=user_id)
    # Grab the book object we want to look up via the passed URL id parameter
    book_look = Book.objects.get(id=book_id)
    # Use the book/bookshelf related_name (declared in model) to see if the book we grabbed in the previous query is on the user's shelf
    # (Can't use user_shelf here because a single object isn't iterable, so we have to define the relationship again for the filter.)
    check_shelf = book_look.on_shelf.filter(owner_id=user_id)

    # Conditional for if the book is on the shelf or not.
    # If it's on the user's shelf:
    if check_shelf:
        # Delete it from the shelf
        user_shelf.shelved.remove(book_look)
    # If not on the shelf:
    else:
        # Add it to the shelf
        book_look.on_shelf.add(user_shelf)

    return HttpResponseRedirect("/bookshelf/" + str(request.user.username))


#####################
## REVIEWS
#####################
#
# Book Reviews view
def reviews(request, book_id):
    user = User.objects.get(id=request.user.id)
    book_look = Book.objects.get(id=book_id)
    reviews = Review.objects.filter(book_reviewed_id=book_id)

    return render(request, "books/reviews.html", { 
        "user": user,
        "book": book_look,
        "reviews": reviews })

# # Creating a new review using Django's generic built-in forms
# class ReviewCreate(CreateView):
#     model = Review
#     fields = "__all__"

#     def form_valid(self, form):
#         self.object = form.save(commit=False)
#         self.object.save()
#         return HttpResponseRedirect("books/<int:book_id>/reviews/" + str(self.object.pk))

# # Editing a review via Django's form
# class ReviewUpdate(UpdateView):
#     model = Review
#     fields = ["subject", "text", "star_rating", "have_finished"]
#     success_url="/"

# # Deleting a review via Django's form
# class ReviewDelete(DeleteView):
#     model = Review
#     # success_url = "/books/<int:book_id>/reviews/"


#####################
## AUTH
#####################
#
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
                    # print(f"req, user: {request}/{user}")
                    return HttpResponseRedirect("/user/" + str(user.username))
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
    # print(f"request, user: {request}, {request.user}")
    logout(request)
    return HttpResponseRedirect("/")

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
        return render(request, "auth/signup.html", { "form": form })

