from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer
from movies_api.mixins import SuccessMessageMixin


class RegisterView(SuccessMessageMixin, generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    success_message = 'User registered successfully.'
