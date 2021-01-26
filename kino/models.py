import datetime

from django.db import models
from django.urls import reverse
from django.template.defaultfilters import truncatechars

from django.contrib.auth.models import User


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
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = ("Клиент")
        verbose_name_plural = ("Клиенты")

    def __str__(self):
        return self.user


# FILM MODELS

YEAR_CHOICES = [(r,r) for r in range(1900, datetime.date.today().year+1)] 

def upload_film_preview(instance, filename):
    return f"films/{instance.name}/preview/{filename}"

def current_year():
    return datetime.date.today().year

class Film(models.Model):

    name = models.CharField(max_length=100, verbose_name='Name', default='')
    year = models.IntegerField(verbose_name='Year', choices=YEAR_CHOICES, default=current_year)
    country = models.CharField(max_length=100, default='', help_text='Country..')
    director = models.CharField(max_length=65, default='', help_text='Director..')
    producer = models.CharField(max_length=65, default='', help_text='Producer..')
    music = models.CharField(max_length=65, default='', help_text='Music By..')
    scenarist = models.CharField(max_length=65, default='', help_text='Written By..')
    genre = models.CharField(max_length=200, default='', help_text='Genre..')
    description = models.TextField(default='', help_text='Describe the plot of the film..')
    preview = models.ImageField(upload_to=upload_film_preview, default='')

    class Meta:
        verbose_name = ("Фильм")
        verbose_name_plural = ("Фильмы")

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("admin_film_detail", kwargs={"pk": self.pk})
    
    def get_absolute_url(self):
        return reverse("admin_films")
    

def upload_film_gallery(instance, filename):
    return f"films/{instance.film.name}/gallery/{filename}"

class FilmGallery(models.Model):

    film = models.ForeignKey(Film, default='', on_delete=models.CASCADE)
    image = models.FileField(upload_to=upload_film_gallery)
    
    class Meta:
        verbose_name = ("Галерея фильма")
        verbose_name_plural = ("Галереи фильмов")
    
    def __str__(self):
        return self.film.name


# CINEMA MODELS

def upload_cinema_preview(instance, filename):
    return f"cinema/{instance.name}/preview/{filename}"

class Cinema(models.Model):

    name = models.CharField(max_length=50, default='', help_text='Дайте название кинотеатру.')
    description = models.TextField(default='', help_text='Опишите кинотеатр, его расположение и/или историю.')
    preview = models.ImageField(upload_to=upload_cinema_preview, default='', help_text='Выберите превью к кинотеатру.')

    class Meta:
        verbose_name = ("Кинотеатр")
        verbose_name_plural = ("Кинотеатры")

    def __str__(self):
        return self.name

def upload_cinema_gallery(instance, filename):
    return f"cinema/{instance.cinema.name}/gallery_of_cinema/{filename}"

class CinemaGallery(models.Model):
    
    cinema = models.ForeignKey(Cinema, default='', on_delete=models.CASCADE)
    images = models.FileField(upload_to=upload_cinema_gallery)
    
    class Meta:
        verbose_name = ("Галерея кинотеатра")
        verbose_name_plural = ("Галереи кинотеатров")
    
    def __str__(self):
        return self.cinema.name

def upload_cinemahall_preview(instance, filename):
    return f"cinema/{instance.cinema.name}/halls/{instance.name}/preview/{filename}"

class CinemaHall(models.Model):

    cinema = models.ForeignKey(Cinema, default='', on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='', help_text='Дайте название залу.')
    description = models.TextField(default='', help_text='Опишите зал.')
    preview = models.ImageField(upload_to=upload_cinemahall_preview, default='', help_text='Выберите превью к залу.')

    class Meta:
        verbose_name = ("Залы кинотеатра")
        verbose_name_plural = ("Залы кинотеатров")

    def __str__(self):
        return f'{self.cinema.name} | {self.name}'

def upload_cinemahall_gallery(instance, filename):
    return f"cinema/{instance.cinema.name}/halls/{instance.hall.name}/gallery/{filename}"

class CinemaHallGallery(models.Model):
    
    cinema = models.ForeignKey(Cinema, default='', on_delete=models.CASCADE)
    hall = models.ForeignKey(CinemaHall, default='', on_delete=models.CASCADE)
    images = models.FileField(upload_to=upload_cinemahall_gallery)
    
    class Meta:
        verbose_name = ("Галерея залов кинотеатра")
        verbose_name_plural = ("Галереи залов кинотеатров ")

    def __str__(self):
        return self.hall.name


# SHARES AND DISCONTS MODEL
class Shares(models.Model):

    shares_name = models.CharField(max_length=50, default='', help_text='Дайте название акции.')
    description = models.TextField(default='', help_text='Опишите условия акции.')
    preview = models.ImageField(upload_to='shares_and_disconts', default='', help_text='Выберите превью к акции.')

    def __str__(self):
        return self.shares_name