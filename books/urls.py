from django.urls import path
from . import views


urlpatterns = [
    path("books/", BookView.as_view()),
    path("books/<uuid:book_id>/", BookDetailView.as_view()),
]
