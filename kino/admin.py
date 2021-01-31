from django.contrib import admin
from django.contrib.auth.models import Group
# from kino.models import Client, Film, Cinema, CinemaHall


# admin.site.unregister(Group)

# class ClientAdmin(admin.ModelAdmin):
#     model = Client


# class FilmGalleryInLine(admin.TabularInline):
#     model = FilmGallery
#     extra = 0
    
# class FilmAdmin(admin.ModelAdmin):
#     inlines = [FilmGalleryInLine]

#     class Meta:
#         model = Film


# class CinemaHallGalleryInLine(admin.TabularInline):
#     model = CinemaHallGallery
#     extra = 0

# class CinemaHallAdmin(admin.ModelAdmin):
#     inlines = [CinemaHallGalleryInLine]


# class CinemaHallInLine(admin.TabularInline):
#     model = CinemaHall
#     extra = 0

# class CinemaGalleryInLine(admin.TabularInline):
#     model = CinemaGallery
#     extra = 0
    
# class CinemaAdmin(admin.ModelAdmin):
#     inlines = [CinemaGalleryInLine, CinemaHallInLine]

#     class Meta:
#         model = Cinema





# admin.site.register(Client, ClientAdmin)
# admin.site.register(Film, FilmAdmin)
# admin.site.register(Cinema, CinemaAdmin)
# admin.site.register(CinemaHall, CinemaHallAdmin)