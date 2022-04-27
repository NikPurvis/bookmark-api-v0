# main_app/views.py

# Import dependencies
from django import http
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist

# Import models
from .models import Book, Bookshelf
from django.contrib.auth.models import User
# Import forms
from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm


# Views (like routes) created below.
# They're functions that are called by main_app's urls.py file.
# Those urls are registered in the project's (bookmark) urls.py.

##################
#  VIEWS
##################

# Index view
def index(request):
    return render(request, "index.html")

# Profile view
def profile(request, username):
    user = User.objects.get(username=username)
    # review = Review.objects.filter(user=user)

    return render(request, "profile.html", { "username": username })
    # , "review": reviews


# Bookshelf view
def bookshelf(request, username):
    print("******************")
    print(connection.queries)
    print("******************")

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
    shelf_books = Book.objects.filter(id__in = found_shelf.title.all().values_list("id"))

    # Test stuff for seeing the SQL queries Django is running.
    # print("******************")
    # print(connection.queries)
    # print("******************")
    # # print("*** bookshelf ***")
    # # print(found_shelf)
    # # print(shelf_books)    
    # print("*** SHELF ID ***")
    # print(found_shelf.owner_id)

    # Passes the filtered bookshelf to the template for display.
    return render(request, "bookshelf.html", {
        "username": username,
        "bookshelf": shelf_books })


# Bookshelf add view
def bookshelf_add(request, book_id):
    user_id = request.user.id
    # check_book = book_id
    # found_shelf = Bookshelf.objects.get(owner_id=user_id)

    book_look = Book.objects.get(id=book_id)
    shelf = book_look.on_shelf.all()
    print(f"shelf: {shelf}")
    
    # print(f"found_book: {found_book}")

    # shelf_books = Bookshelf.objects.filter(check_book__in = found_shelf)
    
    


    # user = User.objects.get(id=request.user.id)
    # # book = Book.objects.get(id=book_id)
    # # found_shelf = Bookshelf.objects.get(owner_id=user.id)
    # shelf_books = Bookshelf.objects.filter(book_id__in = Bookshelf.objects.filter(owner_id=user.id))
    # # .filter(book_id__in = Bookshelf.book_id)
    # print(f"user: {user}")
    # print(f"shelf_books: {shelf_books}")
    
    # if the book is on the bookshelf, show message
    # if the book isn't on the shelf, add it to the shelf
    

    # print("** shelf_books")
    # print(shelf_books)


    return HttpResponse("<p>Bookshelf add</p>")


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


##################
#  CLASSES
##################

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

