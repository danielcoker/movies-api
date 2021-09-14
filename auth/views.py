from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, LoginSerializer
from movies_api.mixins import SuccessMessageMixin


class RegisterView(SuccessMessageMixin, generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    success_message = 'User registered successfully.'


class LoginView(SuccessMessageMixin, APIView):
    success_message = 'User logged in successfully.'

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        password = serializer.validated_data['password']

        user = User.objects.filter(email=email).first()

        if not user:
            return Response({'detail': 'Incorrect email or password.'}, status=400)

        if not check_password(password, user.password):
            return Response({'detail': 'Incorrect email or password.'}, status=400)

        token, created = Token.objects.get_or_create(user=user)

        return Response({'token': token.key, 'user': RegisterSerializer(user).data})
