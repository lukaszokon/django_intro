from django.urls import path
from .views import hello, hello_template, movies


urlpatterns = [
    path('hello', hello),
    path('movies', movies, name='movies'),
    path('', hello_template, name='home'),
]