from django.contrib.auth.forms import UserCreationForm

from .models import LibraryUser


class LibraryUserCreationForm(UserCreationForm):
    class Meta:
        model = LibraryUser
        fields = ('username', 'full_name', 'phone_number')

    def __init__(self, *args, **kwargs):
        """avoiding standart django help text"""
        super(LibraryUserCreationForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'full_name', 'phone_number', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
