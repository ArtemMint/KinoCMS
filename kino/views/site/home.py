from django.shortcuts import redirect, render
from ...repositories.film import get_all_films
from ...repositories.pages import get_home_page
from kino.models.image import FilmImage


def home_page_view(request):
    gallery = FilmImage.objects.filter(film=1)  # should be slider banner on Home page
    return render(request, 'kino/home.html',
                  {"films": get_all_films(),
                   "home_page": get_home_page(),
                   'gallery': gallery})
