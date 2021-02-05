from django.db import models
from django.urls import reverse

from django.contrib.auth.models import User


class Client(models.Model):
    GENDER_CHOICES = [
        ('Мale', 'Male'),
        ('Female', 'Female'),
    ]

    LANGUAGE_CHOICES = [
        ('UA', 'Ukrainian'),
        ('RU', 'Russian'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True, null=True)
    num_card = models.CharField(max_length=16, blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f'{self.user}'

    def get_absolute_url(self):
        return reverse("admin_users")