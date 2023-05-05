from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsEmployeeOrReadOnly, IsEmployee
from .models import Book
from .serializers import BookSerializer


class BookView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployeeOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_url_kwarg = "book_id"

    def get_queryset(self):
        return Book.objects.filter(id=self.kwargs.get("book_id"))
    
class BookDeleteView(generics.DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]

    queryset = Book.objects.all()
    lookup_url_kwarg = "user_id"
