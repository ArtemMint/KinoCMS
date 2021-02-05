from django.db import models
from django.urls import reverse

from utils import current_year


def upload_film_preview(instance, filename):
    return f"films/{instance.name}/preview/{filename}"


def upload_film_gallery(instance, filename):
    return f"films/{instance.name}/gallery/{filename}"


YEAR_CHOICES = [(r, r) for r in range(1900, current_year() + 1)]


class Film(models.Model):
    name = models.CharField(max_length=100, verbose_name='Name', default='')
    year = models.IntegerField(verbose_name='Year', choices=YEAR_CHOICES, default=current_year())
    country = models.CharField(max_length=100, default='')
    director = models.CharField(max_length=65, default='')
    producer = models.CharField(max_length=65, default='')
    music = models.CharField(max_length=65, default='')
    scenarist = models.CharField(max_length=65, default='')
    genre = models.CharField(max_length=200, default='')
    description = models.TextField(default='')
    video = models.URLField(blank=True)
    preview = models.ImageField(upload_to=upload_film_preview, blank=True)
    image1 = models.ImageField(upload_to=upload_film_gallery, blank=True)
    image2 = models.ImageField(upload_to=upload_film_gallery, blank=True)
    image3 = models.ImageField(upload_to=upload_film_gallery, blank=True)
    image4 = models.ImageField(upload_to=upload_film_gallery, blank=True)
    image5 = models.ImageField(upload_to=upload_film_gallery, blank=True)
    seo_title = models.CharField(max_length=50, blank=True)
    seo_keywords = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("admin_films")
