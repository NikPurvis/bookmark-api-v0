# main_app/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    publication = models.CharField(max_length=4)
    description = models.TextField()
    isbn = models.CharField(max_length=13)
    genre = models.CharField(max_length=100)
    olid = models.CharField(max_length=25)

    def __str__(self):
        return self.title


class Bookshelf(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    title = models.ManyToManyField(Book, related_name="on_shelf")
    # Accounting for the difference in singular and plural forms of "bookshelf"
    class Meta:
        verbose_name = ("bookshelf")
        verbose_name_plural = ("bookshelves")
    # Custom display for bookshelf when shown in the admin panel, so it won't just be primary key numbers
    def __str__(self):
        return "Bookshelf for %s" % self.owner
    # Defining the absolute url, which will allow reverse() and  enable linking without hard coding
    def get_absolute_url(self):
        return reverse("bookshelf_detail", kwargs={"bookshelf_id": self.id})



class Review(models.Model):
    class Stars(models.IntegerChoices):
        STAR_0 = 0, "0 stars"
        STAR_1 = 1, "1 star"
        STAR_2 = 2, "2 stars"
        STAR_3 = 3, "3 stars"
        STAR_4 = 4, "4 stars"
        STAR_5 = 5, "5 stars"
    
    title = models.ForeignKey(Book, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(editable=False)
    subject = models.CharField(max_length=255)
    text = models.TextField()
    star_rating = models.PositiveSmallIntegerField(choices=Stars.choices, help_text="How would you rate this book?")
    finished = models.BooleanField

    # Defining a custom save method to override the defaults and inject the data we want
    def save(self, *args, **kwargs):
        # Automatically populate the creation field with the current timestamp on creation (ie, the review doesn't have an id)
        if not self.id:
            self.created = timezone.now()
        # Calls the "real" save method
        return super(User, self).save(*args, **kwargs)

