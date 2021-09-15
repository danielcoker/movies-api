from django.urls import path
from .views import ListCreateMovieView, RetrieveUpdateDestroyMovieView

urlpatterns = [
    path('<int:pk>/', RetrieveUpdateDestroyMovieView.as_view(),
         name='retrieve_update_destroy_movie'),
    path('', ListCreateMovieView.as_view(), name='list_create_movie'),
]
