from django.urls import path
from .views import BookView, BookDetailView


url_patterns = [
    path("books/", BookView.as_view()),
    path("books/<uuid:book_id>/", BookDetailView.as_view()),
]
