from django.contrib.auth.views import (
    LoginView,
)
from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path(
        'signup/', views.SignUp.as_view(), name='signup'
    ),
    path(
        'validate_username',
        views.validate_username,
        name='validate_username'
        ),
    path(
        'validate_phone_number',
        views.validate_phone_number,
        name='validate_phone_number'
        ),
    path(
        'login/',
        LoginView.as_view(
            template_name='users/login.html'),
        name='login'
    ),
]
