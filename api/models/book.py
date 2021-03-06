# api/models/book.py

from django.db import models
from django.contrib.auth import get_user_model

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    publication = models.CharField(max_length=4)
    description = models.TextField()
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def as_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "publication": self.publication,
            "description": self.description,
            "isbn": self.isbn,
            "genre": self.genre
        }
