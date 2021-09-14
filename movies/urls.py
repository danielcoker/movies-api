from django.urls import path
from .views import ListCreateMovieView

urlpatterns = [
    path('', ListCreateMovieView.as_view(), name='list_create_movies'),
]
