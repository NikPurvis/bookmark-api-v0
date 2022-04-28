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

from ..serializers import BookSerializer, ReviewSerializer


# Import models
from ..models import Book, Bookshelf, Review
from django.contrib.auth.models import User
# Import forms
# from .forms import LoginForm
from django.contrib.auth.forms import UserCreationForm


# Views (like routes) created below.
# They're functions that are called by the backend urls.py file.
# Those urls are then registered in the frontend's urls.py.
# In other words, they're functions that take in web requests and return web responses.

class Reviews(ListCreateAPIView):
    # """Class for Index and Post"""
        # """Index review"""
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def post(self, request):
        # """Create review"""
        print(request.data)
        review = ReviewSerializer(data=request.data)
        if review.is_valid():
            review.save()
            return Response(review.data, status=status.HTTP_201_CREATED)
        else:
            return Response(review.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetail(RetrieveUpdateDestroyAPIView):

    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    def get(self, request, pk):
        # """Show one review"""
        review = get_object_or_404(Review, pk=pk)
        data = ReviewSerializer(review).data
        return Response(data)
    
    def delete(self, request, pk):
        # """Deletes a review"""
        review = get_object_or_404(Review, pk=pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def patch(self, request, pk):
        # """Update a review"""
        # first we locate the review
        review = get_object_or_404(Review, pk=pk)
        # then we run our update through the serializer
        updated_review = ReviewSerializer(review, data=request.data)
        if updated_review.is_valid():
            updated_review.save()
            return Response(updated_review.data)
        return Response(updated_review.errors, status=status.HTTP_400_BAD_REQUEST)




# # Book Reviews view
# def reviews(request, book_id):
#     user = User.objects.get(id=request.user.id)
#     book_look = Book.objects.get(id=book_id)
#     reviews = Review.objects.filter(book_reviewed_id=book_id)

#     return render(request, "books/reviews.html", { 
#         "user": user,
#         "book": book_look,
#         "reviews": reviews })

# # # Creating a new review using Django's generic built-in forms
# # class ReviewCreate(CreateView):
# #     model = Review
# #     fields = "__all__"

# #     def form_valid(self, form):
# #         self.object = form.save(commit=False)
# #         self.object.save()
# #         return HttpResponseRedirect("books/<int:book_id>/reviews/" + str(self.object.pk))

# # # Editing a review via Django's form
# # class ReviewUpdate(UpdateView):
# #     model = Review
# #     fields = ["subject", "text", "star_rating", "have_finished"]
# #     success_url="/"

# # # Deleting a review via Django's form
# # class ReviewDelete(DeleteView):
# #     model = Review
# #     # success_url = "/books/<int:book_id>/reviews/"


