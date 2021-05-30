from django.shortcuts import render
from rest_framework import viewsets
from viewer.models import Movie, Genre
from .serializers import MovieListSerializer, MovieRetreiveSerializer, GenreSerializer
from rest_framework import permissions


class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieListSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial-update', 'destroy']:
            self.permission_classes = [permissions.IsAdminUser]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

    def list(self, request, *args, **kwargs):
        self.serializer_class = MovieListSerializer
        return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = MovieRetreiveSerializer
        return super().retrieve(request, *args, **kwargs)


class GenreViewset(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial-update', 'destroy']:
            self.permission_classes = [permissions.IsAdminUser]
        else:
            self.permission_classes = [permissions.AllowAny]
        return super().get_permissions()

# Create your views here.
