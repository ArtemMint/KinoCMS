from django.shortcuts import redirect, render, \
    get_object_or_404

from kino.models.film import Film
from kino.models.image import FilmImage
from kino.models.pages import HomePage


def home_page_view(request):

    films = Film.objects.all()
    # should be slider banner on Home page
    gallery = FilmImage.objects.filter(film=1)
    home_page = HomePage.objects.get(id=0)

    context = {
        "films": films, "home_page": home_page, 'gallery': gallery
    }
    template_name = 'kino/home.html'
    return render(request, template_name, context)
