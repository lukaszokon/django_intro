from logging import getLogger
from operator import attrgetter

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import MovieForm, GenreForm
from .models import Movie, Genre

LOGGER = getLogger()


class GenreDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'genre_delete.html'
    model = Genre
    success_url = reverse_lazy('genres')


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'movie_delete.html'
    model = Movie
    success_url = reverse_lazy('movies')


class MovieUpdateView(LoginRequiredMixin, UpdateView):

    template_name = 'movie_form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('movies')

    def form_invalid(self, form):
        LOGGER.warning('Użyszkodnik wprowadził błędne dane')
        return super().form_invalid(form)


class GenreUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'genre_form.html'
    model = Genre
    form_class = GenreForm
    success_url = reverse_lazy('genres')

    def form_invalid(self, form):
        LOGGER.warning('Użytkownik przesłał nieprawidłowe dane')
        return super().form_invalid(form)





class GenreCreateView(LoginRequiredMixin, CreateView):
    template_name = 'genre_form.html'
    form_class = GenreForm
    success_url = reverse_lazy('genres')

    def form_invalid(self, form):
        LOGGER.warning('Użytkownik przesłał nieprawidłowe dane')
        return super().form_invalid(form)


class MovieCreateView(LoginRequiredMixin, CreateView):
    template_name = 'movie_form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')

    def form_invalid(self, form):
        LOGGER.warning('Użytkownik przesłał nieprawidłowe dane')
        return super().form_invalid(form)


class MovieView(ListView):
    template_name = 'movies.html'
    paginate_by = 5
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
