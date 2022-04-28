# library/serializers.py

# import serializers from the Django REST framework
from rest_framework import serializers
# Import models
# from .models import Book, Bookshelf, Review
from .models.book import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model to define the fields
        model = Book
        # The fields to be returned
        fields = ["title", "author", "publication", "isbn", "genre", "olid", "description"]

# class BookshelfSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Bookshelf
#         fields = ["owner", "shelved"]

# class ReviewSerializer(serializers.ModelSerializer):
#     book_reviewed = BookSerializer(many=True)
#     class Meta:
#         model = Review
#         fields = ("book_reviewed", "subject", "text", "star_rating", "have_finished")
