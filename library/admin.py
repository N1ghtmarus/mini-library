from django.contrib import admin

from .models import Book


@admin.register(Book)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'created', 'updated']
    list_filter = ['created', 'updated']
    list_editable = ['price']
