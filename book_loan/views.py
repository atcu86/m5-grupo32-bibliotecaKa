from rest_framework import generics
from .serializers import BookLoanSerializer
from django.shortcuts import get_object_or_404
from book_copy.models import BookCopy
from books.models import Book
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import date, timedelta


class BookLoanView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = BookLoanSerializer

    lookup_url_kwarg = "bookloan_id"

    def perform_create(self, serializer):
        books = get_object_or_404(Book, id=self.kwargs["bookloan_id"])

        book_copy = BookCopy.objects.all()

        devolution_book = date.today() + timedelta(books.days_to_borrow)

        if devolution_book.weekday() == 5:
            devolution_book = date.today() + timedelta(books.days_to_borrow + 2)
        if devolution_book.weekday() == 6:
            devolution_book = date.today() + timedelta(books.days_to_borrow + 1)

        for book in book_copy:
            if book.book_id == books.id:
                if book.is_available:
                    serializer.save(
                        book_copy=book,
                        user=self.request.user,
                        max_return_date=devolution_book.strftime("%Y-%m-%d"),
                    )


class BookLoanDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = BookLoanSerializer
