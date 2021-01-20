from django.contrib import admin
from django.contrib.auth.models import Group
from kino.models import Client, Film, FilmGallery


admin.site.unregister(Group)

class ClientAdmin(admin.ModelAdmin):
    model = Client
    fields = ('username','city')


class FilmGalleryInLine(admin.TabularInline):
    model = FilmGallery
    extra = 0
    
class FilmAdmin(admin.ModelAdmin):
    inlines = [FilmGalleryInLine]

    class Meta:
        model = Film

admin.site.register(Client, ClientAdmin)
admin.site.register(Film, FilmAdmin)