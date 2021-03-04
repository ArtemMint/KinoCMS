from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.html import mark_safe

from utils import current_year


def upload_film_preview(instance, filename):
    return f"films/{instance.name}/preview/{filename}"


YEAR_CHOICES = [(r, r) for r in range(1900, current_year() + 1)]

GENRES = (
    (1, 'Sci-Fi'),
    (2, 'Detective'),
    (3, 'Horror'),
    (4, 'Anime'),
    (5, 'Thriller'),
)


class Film(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name='Name',
        default='',
    )
    year = models.IntegerField(
        verbose_name='Year',
        choices=YEAR_CHOICES,
        default=timezone.now().year
    )
    country = models.CharField(
        max_length=100,
        default=''
    )
    director = models.CharField(
        max_length=65,
        default=''
    )
    producer = models.CharField(
        max_length=65,
        default=''
    )
    music = models.CharField(
        verbose_name='Music By:',
        max_length=65,
        default='')
    scenarist = models.CharField(
        verbose_name='Written By:',
        max_length=65,
        default=''
    )
    genre = models.CharField(
        max_length=50,
        null=True
    )
    description = models.TextField(
        max_length=1000,
        default=''
    )
    video = models.URLField(
        blank=True
    )
    premiere = models.DateField(
        editable=True,
        default=timezone.now
    )
    preview = models.FileField(
        upload_to=upload_film_preview
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
        return f"{self.name}"

    def image_tag(self):
        return mark_safe(
            '<img src="/directory/%s" width="150" height="150" />'
            % (self.preview))

    def get_absolute_url(self):
        return reverse("admin_films")

    def get_premiere(self):
        if self.premiere >= timezone.now().date():
            return True
        else:
            return False

    def get_current(self):
        if self.premiere < timezone.now().date():
            return True
        else:
            return False
