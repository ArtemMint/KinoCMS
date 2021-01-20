from django.db import models
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
    gender = models.CharField(max_length=1,choices=GENDER_CHOICES, blank=True)
    language = models.CharField(max_length=2,choices=LANGUAGE_CHOICES, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    city = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username


# FILM MODELS
class Film(models.Model):

    name = models.CharField(max_length=100, default='', help_text='Напишите название фильма или мультфильма.')
    country = models.CharField(max_length=100, default='', help_text='Страна съемки..')
    genre = models.CharField(max_length=200, default='', help_text='Жанр..')
    director = models.CharField(max_length=65, default='', help_text='Режисер..')
    description = models.TextField(default='', help_text='Опишите фильма или мультфильма.')
    preview = models.ImageField(upload_to='films', default='', help_text='Выберите превью к фильму.')

    def __str__(self):
        return self.name

def upload_film_gallery(instance, filename):
    return f"films/{instance.film.name}/gallery/{filename}"

class FilmGallery(models.Model):
    film = models.ForeignKey(Film, default='', on_delete=models.CASCADE)
    images = models.FileField(upload_to=upload_film_gallery)
    
    class Meta:
        verbose_name = ("FilmGallery")
        verbose_name_plural = ("FilmGallery")
    
    def __str__(self):
        return self.film.name
    

# CINEMA MODELS
class Cinema(models.Model):
    cinema_name = models.CharField(max_length=50, default='', help_text='Дайте название кинотеатру.')
    description = models.TextField(default='', help_text='Опишите кинотеатр, его расположение и/или историю.')
    preview = models.ImageField(upload_to='cinema', default='', help_text='Выберите превью к кинотеатру.')
    # cinema_gallery = 

    def __str__(self):
        return self.cinema_name

class CinemaHall(models.Model):
    cinema = models.OneToOneField(Cinema, on_delete=models.CASCADE)
    cinemahall_name = models.CharField(max_length=50, default='', help_text='Дайте название залу.')
    description = models.TextField(default='', help_text='Опишите зал.')
    preview = models.ImageField(upload_to='cinema_halls', default='', help_text='Выберите превью к залу.')
    # cinema_hall_gallery = 

    def __str__(self):
        return self.cinemahall_name


# SHARES AND DISCONTS MODEL
class Shares(models.Model):
    shares_name = models.CharField(max_length=50, default='', help_text='Дайте название акции.')
    description = models.TextField(default='', help_text='Опишите условия акции.')
    preview = models.ImageField(upload_to='shares_and_disconts', default='', help_text='Выберите превью к акции.')

    def __str__(self):
        return self.shares_name


