from django.urls import path
from .views import CreateMovieView

urlpatterns = [
    path('', CreateMovieView.as_view(), name='create_movie')
]
