from django.shortcuts import render, redirect, \
    get_object_or_404, get_list_or_404
from django.views.generic import DetailView

from kino.models.film import Film
from kino.models.image import FilmImage
from kino.models.pages import HomePage


def film_detail_view(request, film_id):
    film = Film.objects.get(id=film_id)
    home_page = HomePage.objects.get(id=0)
    gallery = FilmImage.objects.filter(film=film)

    template_name = 'kino/film_detail.html'
    context = {"film": film,
               "home_page": home_page, 'gallery': gallery}

    return render(request, template_name, context)


def premiere_view(request):
    film_list = Film.objects.all()
    home_page = HomePage.objects.get(id=0)

    template_name = 'kino/premiere.html'
    context = {"film_list": film_list, "home_page": home_page}
    return render(request, template_name, context)
