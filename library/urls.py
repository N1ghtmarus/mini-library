from django.urls import path

from . import views


app_name = 'library'

urlpatterns = [
    path('', views.ListBooks.as_view(), name='books_list'),
    path(
        'book/<int:pk>/',
        views.BookDetail.as_view(),
        name='book_detail'
        ),
    path(
        'book_add/',
        views.BookAdd,
        name='book_add'
        ),
]
