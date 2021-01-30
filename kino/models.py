import datetime

from django.utils import timezone
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

    def __str__(self):
        return self.user


# FILM MODELS
YEAR_CHOICES = [(r,r) for r in range(1900, datetime.date.today().year+1)] 

def upload_film_preview(instance, filename):
    return f"films/{instance.name}/preview/{filename}"

def upload_film_gallery(instance, filename):
    return f"films/{instance.name}/gallery/{filename}"

def current_year():
    return datetime.date.today().year

class Film(models.Model):

    name = models.CharField(max_length=100, verbose_name='Name', default='')
    year = models.IntegerField(verbose_name='Year', choices=YEAR_CHOICES, default=current_year)
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
        return self.name
    
    def get_absolute_url(self):
        return reverse("admin_films")

# CINEMA MODELS

def upload_cinema_preview(instance, filename):
    return f"cinema/{instance.name}/preview/{filename}"

def upload_cinema_gallery(instance, filename):
    return f"cinema/{instance.name}/gallery_of_cinema/{filename}"

def upload_cinema_logo(instance, filename):
    return f"cinema/{instance.name}/logo_of_cinema/{filename}"

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
        return self.name

    def get_absolute_url(self):
        return reverse("admin_cinemas")

def upload_cinemahall_preview(instance, filename):
    return f"cinema/{instance.cinema.name}/halls/{instance.name}/preview/{filename}"

def upload_cinemahall_gallery(instance, filename):
    return f"cinema/{instance.cinema.name}/halls/{instance.name}/gallery/{filename}"

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


#   NEWS MODEL
def upload_news_preview(instance, filename):
    return f"news/{instance.name}/preview/{filename}"

def upload_news_gallery(instance, filename):
    return f"news/{instance.name}/gallery_of_news/{filename}"

class News(models.Model):

    name = models.CharField(max_length=50, default='')
    pub_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    preview = models.ImageField(upload_to=upload_news_preview, null=True)
    image1 = models.ImageField(upload_to=upload_news_gallery, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_news_gallery, blank=True, null=True)
    image3 = models.ImageField(upload_to=upload_news_gallery, blank=True, null=True)
    image4 = models.ImageField(upload_to=upload_news_gallery, blank=True, null=True)
    image5 = models.ImageField(upload_to=upload_news_gallery, blank=True, null=True)
    video = models.URLField(blank=True)
    seo_title = models.CharField(max_length=50, blank=True)
    seo_keywords = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("admin_news")


#   SHARES MODEL
def upload_shares_preview(instance, filename):
    return f"shares/{instance.name}/preview/{filename}"

def upload_shares_gallery(instance, filename):
    return f"shares/{instance.name}/gallery_of_shares/{filename}"

class Shares(models.Model):

    name = models.CharField(max_length=50, default='')
    pub_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    preview = models.ImageField(upload_to=upload_shares_preview)
    image1 = models.ImageField(upload_to=upload_shares_gallery, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_shares_gallery, blank=True, null=True)
    image3 = models.ImageField(upload_to=upload_shares_gallery, blank=True, null=True)
    image4 = models.ImageField(upload_to=upload_shares_gallery, blank=True, null=True)
    image5 = models.ImageField(upload_to=upload_shares_gallery, blank=True, null=True)
    video = models.URLField(blank=True)
    seo_title = models.CharField(max_length=50, blank=True)
    seo_keywords = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("admin_shares")