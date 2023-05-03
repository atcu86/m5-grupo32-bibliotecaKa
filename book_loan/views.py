from rest_framework import generics
from .serializers import BookLoanSerializer
from django.shortcuts import get_object_or_404
from book_copy.models import BookCopy
from rest_framework_simplejwt.authentication import JWTAuthentication


class BookLoanView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]

    serializer_class = BookLoanSerializer

    def perform_create(self, serializer):
        book_loan = get_object_or_404(BookCopy, id=self.kwargs['pk'])
        serializer.save(book=book_loan, user=self.request.user)


class BookLoanDetailView(generics.RetrieveUpdateAPIView):
    ...
