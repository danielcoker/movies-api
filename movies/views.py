from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from movies_api.mixins import SuccessMessageMixin
from .models import Movie
from .serializers import MovieSerializer


class CreateMovieView(SuccessMessageMixin, CreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    success_message = 'Movie created successfully.'

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
