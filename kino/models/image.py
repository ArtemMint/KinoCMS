from django.db import models

from kino.models.film import Film
from kino.models.cinema import Cinema, CinemaHall
from kino.models.news import News
from kino.models.shares import Shares


class FilmImage(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images')


class CinemaImage(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images')


class CinemaHallImage(models.Model):
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images')


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images')


class SharesImage(models.Model):
    shares = models.ForeignKey(Shares, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images')
