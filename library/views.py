from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Book
from .forms import BookAddForm


class ListBooks(ListView):
    """View-класс для просмотра всех книг"""
    model = Book
    template_name = 'library_app/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class BookDetail(DetailView):
    """View-класс конкретной книги"""
    model = Book
    template_name = 'library_app/detail.html'
    context_object_name = 'book'


@login_required
def BookAdd(request):
    """View-функция, позволяющая добавить книгу в библиотеку"""
    template = 'library_app/add.html'
    user = request.user
    form = BookAddForm(
        request.POST or None,
        files=request.FILES or None,
    )
    if form.is_valid():
        book = form.save(commit=False)
        book.user = user
        book.save()

    return render(request, template, {'form': form})
