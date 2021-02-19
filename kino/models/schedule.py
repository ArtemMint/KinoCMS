from django.db import models
from django.utils import timezone

from kino.models.film import Film
from kino.models.cinema import CinemaHall


class Schedule(models.Model):

    film = models.ForeignKey(Film, null=True, on_delete=models.CASCADE)
    cinemahall = models.ForeignKey(
        CinemaHall, null=True, on_delete=models.CASCADE, verbose_name='Hall:')
    date = models.DateField(editable=True, null=True, default=timezone.now)
    time = models.TimeField(editable=True, null=True, default=timezone.now, verbose_name='Start time:')
