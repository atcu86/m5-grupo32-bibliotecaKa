from rest_framework import generics
from .serializers import BookLoanSerializer
from django.shortcuts import get_object_or_404
from book_copy.models import BookCopy
from books.models import Book
from rest_framework_simplejwt.authentication import JWTAuthentication
from datetime import date, timedelta
from rest_framework import serializers
from .permissions import IsEmployeeOrOwner
from .models import BookLoan


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

        aux = False

        for book in book_copy:
            if book.book_id == books.id:
                if book.is_available:
                    aux = True
                    serializer.save(
                        book_copy=book,
                        user=self.request.user,
                        max_return_date=devolution_book.strftime("%Y-%m-%d"),
                    )
                    book.is_available = False
                    book.save()
                    break
        if not aux:
            raise serializers.ValidationError({"message": "The book isn't available"})


class BookLoanDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = BookLoanSerializer


class UserHistoryView(generics.ListAPIView):
    serializer_class = BookLoanSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrOwner]
    queryset = BookLoan.objects.all()
    serializer_class = BookLoanSerializer
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        all_loans = BookLoan.objects.filter(user_id=self.kwargs.get("user_id"))
        return all_loans
