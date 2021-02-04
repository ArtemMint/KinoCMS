from django.db import models
from django.urls import reverse


def upload_cinema_preview(instance, filename):
    return f"cinema/{instance.name}/preview/{filename}"


def upload_cinema_gallery(instance, filename):
    return f"cinema/{instance.name}/gallery_of_cinema/{filename}"


def upload_cinema_logo(instance, filename):
    return f"cinema/{instance.name}/logo_of_cinema/{filename}"


def upload_cinemahall_preview(instance, filename):
    return f"cinema/{instance.cinema.name}/halls/{instance.name}/preview/{filename}"


def upload_cinemahall_gallery(instance, filename):
    return f"cinema/{instance.cinema.name}/halls/{instance.name}/gallery/{filename}"


class Cinema(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.TextField(blank=True)
    conditions = models.TextField(blank=True)
    logo = models.ImageField(upload_to=upload_cinema_logo, blank=True)
    preview = models.ImageField(upload_to=upload_cinema_preview, blank=True)
    image1 = models.FileField(upload_to=upload_cinema_gallery, blank=True)
    image2 = models.FileField(upload_to=upload_cinema_gallery, blank=True)
    image3 = models.FileField(upload_to=upload_cinema_gallery, blank=True)
    image4 = models.FileField(upload_to=upload_cinema_gallery, blank=True)
    image5 = models.FileField(upload_to=upload_cinema_gallery, blank=True)
    seo_title = models.CharField(max_length=50, blank=True)
    seo_keywords = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("admin_cinemas")


class CinemaHall(models.Model):
    cinema = models.ForeignKey(Cinema, default='', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='')
    description = models.TextField(blank=True)
    scheme = models.ImageField(upload_to=upload_cinemahall_preview, blank=True)
    preview = models.ImageField(upload_to=upload_cinemahall_preview, blank=True)
    image1 = models.FileField(upload_to=upload_cinemahall_gallery, blank=True)
    image2 = models.FileField(upload_to=upload_cinemahall_gallery, blank=True)
    image3 = models.FileField(upload_to=upload_cinemahall_gallery, blank=True)
    image4 = models.FileField(upload_to=upload_cinemahall_gallery, blank=True)
    image5 = models.FileField(upload_to=upload_cinemahall_gallery, blank=True)
    seo_title = models.CharField(max_length=50, blank=True)
    seo_keywords = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.cinema.name} | {self.name}'
