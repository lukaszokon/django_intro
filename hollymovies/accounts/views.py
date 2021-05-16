from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
from .forms import SignUpForm, ProfileForm
from django.contrib.auth.models import User
from .models import Profile


class SubmittableLoginView(LoginView):
    template_name = 'login.html'


class SubmittablePasswordChangeView(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('movies')


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('movies')


class ProfileDeleteView(DeleteView):

    template_name = 'profile_delete.html'
    model = User
    success_url = reverse_lazy('movies')

    def get_object(self, queryset=None):
        return self.request.user


class ProfileDetailView(DetailView):

    template_name = 'profile_detail.html'
    model = User

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if Profile.objects.filter(user=self.request.user).exists():
            profile = Profile.objects.get(user=self.request.user)
            context['biography'] = profile.biography
        return context


class ProfileUpdateView(UpdateView):

    template_name = 'profile-update.html'
    model = User
    form_class = ProfileForm
    success_url = reverse_lazy('profile-detail')

    def get_object(self, queryset=None):
        return self.request.user


