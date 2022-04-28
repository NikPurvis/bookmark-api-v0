# library/urls.py

# Import dependencies
from django.urls import path
from .views.book_views import Books, BookDetail
# from .views.review_views import Reviews, ReviewDetail
from .models.book import Book

urlpatterns = [
    
    path("", Books.as_view(), name="Books"),
    path("<int:pk>/", BookDetail.as_view(), name="Book-detail"),
    # path("reviews", Reviews.as_view(), name="Reviews"),
    # path("reviews/<int:pk", ReviewDetail.as_view(), name="Review-detail")
]



# # Mapping the views to URLs
# urlpatterns = [
#     #####################
#     ##  ROOT
#     #####################
#     path("", views.index, name="books"),



    
    # #####################
    # ##  AUTH
    # #####################
    # path("login/", views.login_view, name="login"),
    # path("logout/", views.logout_view, name="logout"),
    # path("signup/", views.signup_view, name="signup"),
    
    # #####################
    # ##  USER
    # #####################    
    # path("user/<username>", views.profile, name="profile"),
    
    # #####################
    # ##  BOOKS
    # #####################
    # path("books/", views.books_index, name="books_index"),
    # path("books/<int:book_id>/", views.books_show, name="books_show"),
    # path("books/create/", views.BookCreate.as_view(), name="book_create"),
    # path("books/<int:pk>/update/", views.BookUpdate.as_view(), name="book_update"),
    # path("books/<int:pk>/delete/", views.BookDelete.as_view(), name="book_delete"),

    # #####################
    # ##  BOOKSHELF
    # #####################
    # path("bookshelf/<username>", views.bookshelf, name="bookshelf"),
    # path("books/<int:book_id>/add", views.bookshelf_add, name="bookshelf_add"),

    # #####################
    # ##  REVIEWS
    # #####################
    # path("books/<int:book_id>/reviews", views.reviews, name="reviews"),

    # # path("books/<int:book_id>/reviews", views.reviews, name="reviews"),
    # # path("books/<int:book_id>/reviews/create/", views.ReviewCreate.as_view(), name="review_create"),
    # # path("books/<int:book_id>/reviews/<int:pk>/update/", views.ReviewUpdate.as_view(), name="review_update"),
    # # path("books/<int:book_id>/reviews/<int:pk>/delete/", views.ReviewDelete.as_view(), name="review_delete"),

    # #####################
    # ##  BOOKCLUB
    # #####################
    # path("bookclub/", views.bookclub, name="bookclub"),

    # #####################
    # ##  SEARCH
    # #####################
    # path("search/", views.search, name="search"),

# ]
