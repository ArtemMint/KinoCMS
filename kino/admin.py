from django.contrib import admin
from kino.models import Client, Film

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    model = Client
    fields = ('username','city')

class FilmAdmin(admin.ModelAdmin):
    model = Film



admin.site.register(Client)
admin.site.register(Film)