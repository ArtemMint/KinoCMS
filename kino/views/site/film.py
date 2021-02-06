from django.views.generic import DetailView, ListView

from kino.models.film import Film


class FilmDetailView(DetailView):
    model = Film
    template_name = 'kino/film_detail.html'


class FilmPremiereView(ListView):
    model = Film
    template_name = 'kino/premiere.html'
