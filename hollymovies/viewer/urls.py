from django.urls import path
from .views import hello, hello_template, movies, MovieView, MovieDetailView


urlpatterns = [
    path('hello', hello),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies', MovieView.as_view(), name='movies'),
    path('', hello_template, name='home'),
]