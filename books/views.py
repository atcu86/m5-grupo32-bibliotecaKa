from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsEmployeeOrReadOnly, IsEmployee
from .models import Book
from .serializers import BookSerializer
from rest_framework import serializers


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        if type(self.request.data["days_to_borrow"]) == int:
            if self.request.data["days_to_borrow"] < 1:
                raise serializers.ValidationError(
                    {"message": "Days to borrow can't be lower then 1."}
                )

        if self.request.data["quantity"] < 1:
            raise serializers.ValidationError(
                {"message": "Quantity can't be lower then 1."}
            )

        return serializer.save()


class BookDetailView(generics.RetrieveDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = "book_id"

    def get_queryset(self):
        return Book.objects.filter(id=self.kwargs.get("book_id"))
