"""Module with Client user"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

import datetime

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField


class Client(models.Model):
    """Client form which extending User model

    Args:
        models ([type]): [description]

    Returns:
        [type]: [description]
    """
    GENDER_CHOICES = [
        ('Unknown', 'Unknown'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    LANGUAGE_CHOICES = [
        ('UA', 'Ukrainian'),
        ('RU', 'Russian'),
    ]

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    address = models.CharField(
        max_length=50,
        null=True
    )
    num_card = models.CharField(
        max_length=20,
        null=True
    )

    birth_date = models.DateField(
        editable=True,
        default=timezone.now,
        null=True
    )

    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        null=True
    )

    language = models.CharField(
        max_length=20,
        choices=LANGUAGE_CHOICES,
        null=True
    )

    phone = PhoneNumberField(
        max_length=13,
        null=True,
        blank=False,
        unique=True
    )

    city = models.CharField(
        max_length=50,
        blank=True,
        null=True
    )

    # USERNAME_FIELD = user.primary_key
    # REQUIRED_FIELDS = []

    def __str__(self):
        """Return string with username
        """
        return f'{self.user}'

    def get_absolute_url(self):
        """Return url after creating user
        """
        return reverse("admin_users")

    def get_age(self):
        """Return age of current user
        """
        if self.birth_date != None:
            return (datetime.date.today() - self.birth_date).days//365
        else:
            return None
