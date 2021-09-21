from django.urls import path
from auth.views import RegisterView, LoginView


urlpatterns = [
    path('/login', LoginView.as_view(), name='auth_login'),
    path('/register', RegisterView.as_view(), name='auth_register')
]
