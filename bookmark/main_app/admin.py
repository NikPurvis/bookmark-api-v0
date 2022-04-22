# Import dependencies
from django.contrib import admin
# Import models
from .models import Book

# Register models
admin.site.register(Book)
