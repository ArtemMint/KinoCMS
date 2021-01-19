from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Film(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(default=' ')
    image = models.ImageField(upload_to='films', help_text='Choose the picture of the film.')


class Client(models.Model):
    
    GENDER_CHOICES = [
        ('М', 'Male'),
        ('F', 'Female'),
        ]

    LANGUAGE_CHOICES = [
        ('UA', 'Ukrainian'),
        ('RU', 'Russian'),
        ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50, blank=True)
    num_card = models.CharField(max_length=16, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES, blank=True)
    language = models.CharField(max_length=2,choices=LANGUAGE_CHOICES, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=50, blank=True)