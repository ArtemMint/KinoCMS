from django.db import models
from django.urls import reverse
from django.utils import timezone
import datetime
from phonenumber_field.modelfields import PhoneNumberField

from django.contrib.auth.models import User


class Client(models.Model):
    GENDER_CHOICES = [
        ('Unknown', 'Unknown'),
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    LANGUAGE_CHOICES = [
        ('UA', 'Ukrainian'),
        ('RU', 'Russian'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, null=True)
    num_card = models.CharField(max_length=20, null=True)
    birth_date = models.DateField(
        editable=True, default=timezone.now, null=True)
    gender = models.CharField(
        max_length=20, choices=GENDER_CHOICES, null=True)
    language = models.CharField(
        max_length=20, choices=LANGUAGE_CHOICES, null=True)
    phone = PhoneNumberField(max_length=13, null=True,
                             blank=False, unique=True)
    city = models.CharField(max_length=50, blank=True, null=True)

    # USERNAME_FIELD = user.primary_key
    # REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.user}'

    def get_absolute_url(self):
        return reverse("admin_users")

    def get_age(self):
        if self.birth_date != None:
            return (datetime.date.today() - self.birth_date).days//365
        else:
            return None
