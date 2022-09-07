from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class LibraryUser(AbstractUser):
    full_name = models.CharField("ФИО", max_length=120, db_index=True)

    phone_regex = RegexValidator(regex=r'^\+?7?\d{11,12}$', message="Некорректный номер телефона")
    phone_number = models.CharField(
                                    "Номер телефона",
                                    validators=[phone_regex],
                                    max_length=14,
                                    unique=True,
                                    blank=False
                                    )

    def __str__(self):
        return self.username
    