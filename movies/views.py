from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
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
