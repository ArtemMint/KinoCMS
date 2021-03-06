from django.utils import timezone
from django.db import models

from kino.models.cinema import Cinema
from phonenumber_field.modelfields import PhoneNumberField


class HomePage(models.Model):
    phone1 = PhoneNumberField(
        null=False,
        blank=False,
        unique=True
    )
    phone2 = PhoneNumberField(
        null=False,
        blank=False,
        unique=True
    )
    seo_text = models.TextField(
        max_length=500
    )
    seo_title = models.CharField(
        max_length=50,
        blank=True
    )
    seo_keywords = models.CharField(
        max_length=100,
        blank=True
    )
    seo_description = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return f'{self.pk}'


class Contacts(models.Model):
    cinema = models.ForeignKey(
        Cinema,
        on_delete=models.CASCADE,
        null=True
    )
    address = models.TextField(
        max_length=200,
        blank=True
    )
    status = models.BooleanField(
        default=False
    )
    coordinates = models.CharField(
        max_length=100
    )
    seo_title = models.CharField(
        max_length=50,
        blank=True
    )
    seo_keywords = models.CharField(
        max_length=100,
        blank=True
    )
    seo_description = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return f'{self.name}'


class Page(models.Model):
    name = models.CharField(
        max_length=50,
        default=''
    )
    description = models.TextField(
        max_length=500,
        blank=True
    )
    status = models.BooleanField(
        default=False
    )
    preview = models.ImageField(
        upload_to='images/preview'
    )
    seo_title = models.CharField(
        max_length=50,
        blank=True
    )
    seo_keywords = models.CharField(
        max_length=100,
        blank=True
    )
    seo_description = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return f'{self.name}'
