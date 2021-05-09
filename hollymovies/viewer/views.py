from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie, Genre
from django.views.generic import ListView, DetailView
from operator import attrgetter


class MovieView(ListView):
    template_name = 'movies.html'
    model = Movie

    def get_queryset(self):
        genre = self.request.GET.get('genre')
        sort = self.request.GET.get('sort')
        if genre:
            queryset = Movie.objects.filter(genre__name=genre)
        else:
            queryset = Movie.objects.all()
        if sort:
            queryset = sorted(queryset, key=attrgetter(sort))
        return queryset


class GenreListView(ListView):
    template_name = 'genres.html'
    model = Genre
    ordering = 'name'


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'


def hello(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello {s} World!')


def hello_template(request):
    s1 = request.GET.get('s1', '')
    return render(request, template_name='hello.html', context={'adjectives': [s1, 'piękny', 'cudowny']})


def movies(request):
    return render(request, template_name='movies.html', context={'movies': Movie.objects.all()})
