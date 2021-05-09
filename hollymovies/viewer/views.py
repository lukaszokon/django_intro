from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie
from django.views.generic import ListView, DetailView


# Create your views here.

class MovieDetailView(DetailView):
    model = Movie
    template_name = 'movie_detail.html'


class MovieView(ListView):
    template_name = 'movies.html'
    model = Movie



def hello(request):
    s = request.GET.get('s', '')
    return HttpResponse(f'Hello {s} World!')


def hello_template(request):
    s1 = request.GET.get('s1', '')
    return render(request, template_name='hello.html', context={'adjectives': [s1, 'piękny', 'cudowny']})


def movies(request):
    return render(request, template_name='movies.html', context={'movies': Movie.objects.all()})
