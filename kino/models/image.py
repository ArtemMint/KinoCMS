from django.db import models
from django.core.validators import RegexValidator

from kino.models.film import Film


class Image(models.Model):

    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images')
