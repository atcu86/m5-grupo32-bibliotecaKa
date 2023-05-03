from django.urls import path
from .views import BookView


url_patterns = [
    path("books/", BookView.as_view()),
    path("books/<uuid:book_id>/", BookView.as_view()),
]
