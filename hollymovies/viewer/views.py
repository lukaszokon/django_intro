from logging import getLogger
from operator import attrgetter

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User

from .forms import MovieForm, GenreForm, CommentForm
from .models import Movie, Genre, Comment

LOGGER = getLogger()


class CommentAuthorRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user == self.get_object().author


class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


class GenreDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'genre_delete.html'
    model = Genre
    success_url = reverse_lazy('genres')
    permission_required = 'viewer.delete_genre'


class MovieDeleteView(StaffRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = 'movie_delete.html'
    model = Movie
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.delete_movie'

    def test_func(self):
        return super().test_func() and self.request.user.is_superuser


class MovieUpdateView(StaffRequiredMixin, PermissionRequiredMixin, UpdateView):

    template_name = 'movie_form.html'
    model = Movie
    form_class = MovieForm
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.change_movie'

    def form_invalid(self, form):
        LOGGER.warning('Użyszkodnik wprowadził błędne dane')
        return super().form_invalid(form)


class GenreUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'genre_form.html'
    model = Genre
    form_class = GenreForm
    success_url = reverse_lazy('genres')
    permission_required = 'viewer.change_genre'

    def form_invalid(self, form):
        LOGGER.warning('Użytkownik przesłał nieprawidłowe dane')
        return super().form_invalid(form)


class GenreCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'genre_form.html'
    form_class = GenreForm
    success_url = reverse_lazy('genres')
    permission_required = 'viewer.add_genre'

    def form_invalid(self, form):
        LOGGER.warning('Użytkownik przesłał nieprawidłowe dane')
        return super().form_invalid(form)


class MovieCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'movie_form.html'
    form_class = MovieForm
    success_url = reverse_lazy('movies')
    permission_required = 'viewer.add_movie'

    def form_invalid(self, form):
        LOGGER.warning('Użytkownik przesłał nieprawidłowe dane')
        return super().form_invalid(form)


class MovieView(PermissionRequiredMixin, ListView):
    template_name = 'movies.html'
    paginate_by = 5
    model = Movie
    permission_required = 'viewer.view_movie'

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


class GenreListView(PermissionRequiredMixin, ListView):
    template_name = 'genres.html'
    model = Genre
    ordering = 'name'
    permission_required = 'viewer.view_genre'


class CommentDeleteView(CommentAuthorRequiredMixin, DeleteView):
    template_name = 'comment_delete.html'
    model = Comment

    def get_success_url(self):
        return reverse_lazy('movie-detail', kwargs={'pk': self.kwargs['movie_pk']})


class CommentUpdateView(CommentAuthorRequiredMixin, UpdateView):
    template_name = 'comment_form.html'
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('movie-detail', kwargs={'pk': self.kwargs['movie_pk']})

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.movie = Movie.objects.get(id=self.kwargs['movie_pk'])
        comment.save()
        return HttpResponseRedirect(self.get_success_url())


class CommentCreateView(CreateView):
    template_name = 'comment_form.html'
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('movie-detail', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.movie = Movie.objects.get(id=self.kwargs['pk'])
        comment.save()
        return HttpResponseRedirect(self.get_success_url())


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        comments = Comment.objects.filter(movie=self.kwargs['pk']).order_by('-created')
        context['comments'] = comments
        return context


def hello(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello {s} World!')


def hello_template(request):
    s1 = request.GET.get('s1', '')
    return render(request, template_name='hello.html', context={'adjectives': [s1, 'piękny', 'cudowny']})


def movies(request):
    return render(request, template_name='movies.html', context={'movies': Movie.objects.all()})
