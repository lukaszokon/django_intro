from django.urls import path
from .views import SubmittableLoginView

urlpatterns = [
    path('login/', SubmittableLoginView.as_view(), name='login'),
]