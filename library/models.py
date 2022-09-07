from django.db import models
from django.urls import reverse

from users.models import LibraryUser


class Book(models.Model):
    """Таблица с книгами сайта"""
    user = models.ForeignKey(
                                LibraryUser,
                                verbose_name='Пользователь',
                                related_name='user',
                                on_delete=models.CASCADE
                                )
    name = models.CharField('Имя книги', max_length=200, db_index=True)
    description = models.TextField('Описание', blank=True)
    image = models.ImageField('Фото', upload_to='books/%Y/%m/%d', blank=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    created = models.DateTimeField('Добавлена', auto_now_add=True)
    updated = models.DateTimeField('Изменена', auto_now=True)

    def get_absolute_url(self):
        return reverse('library:book_detail', args=[self.pk])

    class Meta:
        ordering = ('-updated',)
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'

    def __str__(self):
        return self.name
