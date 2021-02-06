from django.views.generic import ListView, DetailView

from kino.models.cinema import Cinema


class CinemasView(ListView):
    model = Cinema
    template_name = 'kino/cinemas.html'


class CinemaDetailView(DetailView):
    model = Cinema
    template_name = 'kino/cinema_detail.html'
