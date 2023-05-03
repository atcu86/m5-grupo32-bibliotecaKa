from rest_framework import generics
from .models import Genre
from .serializers import GenreSerializer


class GenreView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
