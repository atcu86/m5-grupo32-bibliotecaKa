from rest_framework import generics
from .serializers import BookLoanSerializer
from django.shortcuts import get_object_or_404
from book_copy.models import BookCopy
from books.models import Book
from rest_framework_simplejwt.authentication import JWTAuthentication


class BookLoanView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = BookLoanSerializer

    lookup_url_kwarg = "bookloan_id"

    def perform_create(self, serializer):
        book_copy = get_object_or_404(BookCopy, id=self.kwargs['bookloan_id'])
        # book = get_object_or_404(BookCopy, book_id=book_copy)

        serializer.save(book_copy=book_copy, user=self.request.user)


class BookLoanDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = BookLoanSerializer
