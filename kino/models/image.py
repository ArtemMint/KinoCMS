from django.db import models

from kino.models.film import Film
from kino.models.cinema import Cinema, CinemaHall
from kino.models.news import News
from kino.models.shares import Shares
from kino.models.pages import Page


class FilmImage(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/film')


class CinemaImage(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/cinema')


class CinemaHallImage(models.Model):
    cinema_hall = models.ForeignKey(CinemaHall, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/cinema_hall')


class NewsImage(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/news')


class SharesImage(models.Model):
    shares = models.ForeignKey(Shares, on_delete=models.CASCADE)
    image = models.FileField(upload_to='images/shares')


class ChildrenRoomImage(models.Model):
    children_room = models.ForeignKey(Page, on_delete=models.ForeignKey)
    image = models.FileField(upload_to='images/children_room')


class CafeBarImage(models.Model):
    cafe_bar = models.ForeignKey(Page, on_delete=models.ForeignKey)
    image = models.FileField(upload_to='images/cafe_bar')

class VipHallImage(models.Model):
    vip_hall = models.ForeignKey(Page, on_delete=models.ForeignKey)
    image = models.FileField(upload_to='images/vip_hall')
