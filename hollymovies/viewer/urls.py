from django.urls import path
from .views import hello, hello_template, movies, MovieView, MovieDetailView, GenreListView, \
    MovieCreateView, GenreCreateView, MovieUpdateView, MovieDeleteView


urlpatterns = [
    path('hello', hello),
    path('movies/new', MovieCreateView.as_view(), name='movie-create'),
    path('movies/update/<int:pk>', MovieUpdateView.as_view(), name='movie-update'),
    path('movies/delete/<int:pk>', MovieDeleteView.as_view(), name='movie-delete'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies', MovieView.as_view(), name='movies'),
    path('genre/new', GenreCreateView.as_view(), name='genre-create'),
    path('genre', GenreListView.as_view(), name='genres'),
    path('', hello_template, name='home'),
]