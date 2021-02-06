from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from kino.forms.cinema import CinemaForm
from kino.models.cinema import Cinema


class AdminCinemasView(ListView):
    model = Cinema
    template_name = 'admin_panel/cinema/cinemas.html'


class AdminCinemaDetailView(DetailView):
    model = Cinema
    template_name = 'admin_panel/cinema/cinema_detail.html'


class AdminCinemaAddView(CreateView):
    model = Cinema
    form_class = CinemaForm
    template_name = 'admin_panel/cinema/cinema_add.html'


class AdminCinemaUpdateView(UpdateView):
    model = Cinema
    form_class = CinemaForm
    template_name = 'admin_panel/cinema/cinema_update.html'


class AdminCinemaDeleteView(DeleteView):
    model = Cinema
    template_name = 'admin_panel/cinema/cinema_delete.html'
    success_url = reverse_lazy('admin_cinemas')