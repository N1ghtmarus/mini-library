from django.contrib import admin

from .models import LibraryUser


@admin.register(LibraryUser)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'full_name', 'phone_number']
    list_filter = ['username', 'full_name']
