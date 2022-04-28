# library/book_views.py

# Import dependencies
from django import http
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.db import connection
from django.core.exceptions import ObjectDoesNotExist


from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status

# Import models
from ..serializers import BookSerializer
from ..models.book import Book

# from ..models import Book, Bookshelf, Review
from django.contrib.auth.models import User
# Import forms
# from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm


# Views (like routes) created below.
# They're functions that are called by the backend urls.py file.
# Those urls are then registered in the frontend's urls.py.
# In other words, they're functions that take in web requests and return web responses.

class Books(ListCreateAPIView):
    # """Class for Index and Post"""
        # """Index Books"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def post(self, request):
        # """Create Books"""
        print(request.data)
        book = BookSerializer(data=request.data)
        if book.is_valid():
            book.save()
            return Response(book.data, status=status.HTTP_201_CREATED)
        else:
            return Response(book.errors, status=status.HTTP_400_BAD_REQUEST)


class BookDetail(RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, pk):
        # """Show one book"""
        book = get_object_or_404(Book, pk=pk)
        data = BookSerializer(book).data
        return Response(data)
    
    def delete(self, request, pk):
        # """Deletes a book"""
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        # """Update a Book"""
        # first we locate the book
        book = get_object_or_404(Book, pk=pk)
        # then we run our update through the serializer
        updated_book = BookSerializer(book, data=request.data)
        if updated_book.is_valid():
            updated_book.save()
            return Response(updated_book.data)
        return Response(updated_book.errors, status=status.HTTP_400_BAD_REQUEST)

