from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView

from kino.forms.film import FilmForm
from kino.models.film import Film


class AdminFilmsView(ListView):
    model = Film
    template_name = 'admin_panel/film/films.html'
    ordering = ['-id']


class AdminFilmDetailView(DetailView):
    model = Film
    template_name = 'admin_panel/film/film_detail.html'


class AdminFilmAddView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'admin_panel/film/film_add.html'


class AdminFilmUpdateView(UpdateView):
    model = Film
    form_class = FilmForm
    template_name = 'admin_panel/film/film_update.html'


class AdminFilmDeleteView(DeleteView):
    model = Film
    template_name = 'admin_panel/film/film_delete.html'
    success_url = reverse_lazy('admin_films')
