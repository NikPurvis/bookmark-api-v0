# Import dependencies
from django.contrib import admin
# Import models
from .models import Book, Bookshelf, Review

# Register models
admin.site.register(Book)
admin.site.register(Bookshelf)
admin.site.register(Review)
