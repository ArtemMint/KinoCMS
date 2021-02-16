from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist

from kino.models.film import Film
from kino.models.image import FilmImage
from kino.models.pages import HomePage


def home_page_view(request):
    films = Film.objects.all()
    gallery = FilmImage.objects.filter(film=1)  # should be slider banner on Home page
    try:
        home_page = HomePage.objects.get(id=0)
    except HomePage.DoesNotExist:
        home_page = None

    context = {
        "films": films, "home_page": home_page, 'gallery': gallery
    }
    template_name = 'kino/home.html'
    return render(request, template_name, context)
