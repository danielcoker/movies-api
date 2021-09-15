from movies.permissions import IsOwnerOrReadOnly
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from movies_api.mixins import SuccessMessageMixin
from .models import Movie
from .serializers import MovieSerializer


class ListCreateMovieView(SuccessMessageMixin, ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def post(self, request, *args, **kwargs):
        self.success_message = 'Movie created successfully.'
        return super().post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.success_message = 'Movie retrieved successfully.'
        return super().get(request, *args, **kwargs)


class RetrieveUpdateDestroyMovieView(SuccessMessageMixin, RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        self.success_message = 'Movie retrieved successfully.'
        return super().get(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        self.success_message = 'Movie updated successfully.'
        return super().put(request, *args, **kwargs)
