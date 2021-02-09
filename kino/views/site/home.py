from django.views.generic import ListView

from kino.models.film import Film


class HomeView(ListView):
    model = Film
    template_name = 'kino/home.html'