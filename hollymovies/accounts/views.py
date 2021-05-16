from django.shortcuts import render
from django.contrib.auth.views import LoginView


class SubmittableLoginView(LoginView):
    template_name = 'login.html'

# Create your views here.
