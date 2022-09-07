from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import LibraryUserCreationForm
from .models import LibraryUser


class SignUp(CreateView):
    form_class = LibraryUserCreationForm
    success_url = reverse_lazy('library:books_list')
    template_name = 'users/signup.html'


def validate_username(request):
    """Проверка доступности логина"""
    username = request.GET.get('username', None)
    response = {
        'is_taken': LibraryUser.objects.filter(username=username).exists()
    }
    return JsonResponse(response)


def validate_phone_number(request):
    """Проверка доступности номера телефона"""
    phone_number = request.GET.get('phone_number', None)
    response = {
        'is_taken': LibraryUser.objects.filter(phone_number=phone_number).exists()
    }
    return JsonResponse(response)
