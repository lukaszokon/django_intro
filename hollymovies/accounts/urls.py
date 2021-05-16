from django.urls import path
from .views import SubmittableLoginView, SubmittablePasswordChangeView, SignUpView, \
    ProfileUpdateView, ProfileDetailView, ProfileDeleteView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', SubmittablePasswordChangeView.as_view(), name='password-change'),
    path('profile-detail/', ProfileDetailView.as_view(), name='profile-detail'),
    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile-delete/', ProfileDeleteView.as_view(), name='profile-delete'),
    path('sign-up/', SignUpView.as_view(), name='sign-up')
]