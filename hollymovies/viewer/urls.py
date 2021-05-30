from django.urls import path
from .views import hello, hello_template, movies, MovieView, MovieDetailView, GenreListView, \
    MovieCreateView, GenreCreateView, MovieUpdateView, MovieDeleteView, GenreDeleteView, GenreUpdateView, \
    CommentCreateView, CommentUpdateView, CommentDeleteView


urlpatterns = [
    path('hello', hello),
    path('movies/new', MovieCreateView.as_view(), name='movie-create'),
    path('movies/update/<int:pk>', MovieUpdateView.as_view(), name='movie-update'),
    path('movies/delete/<int:pk>', MovieDeleteView.as_view(), name='movie-delete'),
    path('movies/<int:pk>/add-comment', CommentCreateView.as_view(), name='comment-add'),
    path('movies/<int:movie_pk>/edit-comment/<int:pk>', CommentUpdateView.as_view(), name='comment-edit'),
    path('movies/<int:movie_pk>/delete-comment/<int:pk>', CommentDeleteView.as_view(), name='comment-delete'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
    path('movies', MovieView.as_view(), name='movies'),
    path('genre/new', GenreCreateView.as_view(), name='genre-create'),
    path('genre/update/<int:pk>', GenreUpdateView.as_view(), name='genre-update'),
    path('genre/delete/<int:pk>', GenreDeleteView.as_view(), name='genre-delete'),
    path('genre', GenreListView.as_view(), name='genres'),
    path('', hello_template, name='home'),
]