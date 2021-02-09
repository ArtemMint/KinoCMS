from django.views.generic import ListView

from kino.models.film import Film


class PosterView(ListView):
    model = Film
    template_name = 'kino/poster.html'