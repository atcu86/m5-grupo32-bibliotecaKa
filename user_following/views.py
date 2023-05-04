from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import UserFollowing
from .serializers import UserFollowingSerializer
from .permissions import IsStudent
from rest_framework import generics
from books.models import Book
from django.shortcuts import get_object_or_404


class UserFollowingView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsStudent]
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowingSerializer
    lookup_url_kwarg = "book_id"


def perform_create(self, serializer):
    book = get_object_or_404(Book, id=self.kwargs.get("book_id"))
    return serializer.save(book=book, user=self.request.user)
