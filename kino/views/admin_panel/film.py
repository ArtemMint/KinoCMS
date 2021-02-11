from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory, modelformset_factory
from django.core.paginator import Paginator

from kino.forms.film import FilmForm
from kino.models.film import Film
from kino.models.image import Image


class AdminFilmsView(ListView):
    model = Film
    template_name = 'admin_panel/film/films.html'
    ordering = ['-id']


def admin_film_detail_view(request, film_id):
    film = Film.objects.get(id=film_id)
    template_name = 'admin_panel/film/film_detail.html'
    context = {'film': film}
    return render(request, template_name, context)


class AdminFilmAddView(CreateView):
    model = Film
    form_class = FilmForm
    template_name = 'admin_panel/film/film_add.html'


def admin_film_update_view(request, film_id):
    FilmFormSet = inlineformset_factory(Film, Image, fields='__all__', extra=5, max_num=5)
    film = Film.objects.get(id=film_id)
    form = FilmForm(instance=film)
    formset = FilmFormSet(instance=film)
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES, instance=film)
        formset = FilmFormSet(request.POST, request.FILES, instance=film)
        if formset.is_valid() and form.is_valid():
            form.save()
            formset.save()
            return redirect('admin_films')

    template_name = 'admin_panel/film/film_update.html'
    context = {'form': form,'formset': formset}
    return render(request, template_name, context)


class AdminFilmDeleteView(DeleteView):
    model = Film
    template_name = 'admin_panel/film/film_delete.html'
    success_url = reverse_lazy('admin_films')
