import datetime

from django.db import models
from django.urls import reverse


def upload_cinema_preview(instance, filename):
    return f"cinema/{instance.name}/preview/{filename}"


def upload_cinema_logo(instance, filename):
    return f"cinema/{instance.name}/logo_of_cinema/{filename}"


def upload_cinemahall_preview(instance, filename):
    return f"cinema/{instance.cinema.name}/halls/{instance.name}/preview/{filename}"


class Cinema(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.TextField(max_length=1000, blank=True)
    conditions = models.TextField(max_length=1000, blank=True)
    logo = models.ImageField(upload_to=upload_cinema_logo, blank=True)
    preview = models.ImageField(upload_to=upload_cinema_preview, blank=True)
    seo_title = models.CharField(max_length=50, blank=True)
    seo_keywords = models.CharField(max_length=100, blank=True)
    seo_description = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("admin_cinemas")


class CinemaHall(models.Model):
    cinema = models.ForeignKey(Cinema, default='', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    created_date = models.DateField(default=datetime.datetime.now)
    description = models.TextField(blank=True)
    scheme = models.ImageField(upload_to='images')
    preview = models.ImageField(upload_to='images')
    seo_title = models.CharField(max_length=50, blank=True)
    seo_keywords = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.name}'
