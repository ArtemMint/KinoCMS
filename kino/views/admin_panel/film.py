from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

from kino.forms.film import FilmForm
from kino.forms.image import FilmImageForm
from kino.models.film import Film
from kino.models.image import FilmImage
from ...repositories.film import get_film_by_id
from ...repositories.image import *


@method_decorator(permission_required('is_staff'), name='dispatch')
class AdminFilmsView(ListView):
    model = Film
    template_name = 'admin_panel/film/films.html'
    ordering = ['-id']
    paginate_by = 15


@permission_required('is_staff')
def admin_film_detail_view(request, film_id):
    return render(
        request,
        'admin_panel/film/film_detail.html',
        {
            'film': get_film_by_id(film_id),
            'gallery': get_film_image_list_by_id(film_id)
        }
    )


@permission_required('is_staff')
def admin_film_create_view(request):
    FilmFormSet = inlineformset_factory(
        Film, FilmImage, fields='__all__', extra=5, max_num=5)

    form = FilmForm()
    formset = FilmFormSet()
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)
        formset = FilmFormSet(request.POST, request.FILES,
                              instance=form.instance)
        if formset.is_valid() and form.is_valid():
            form.save()
            formset.save()
            return redirect('admin_films')

    return render(
        request,
        'admin_panel/film/film_add.html',
        {
            'form': form,
            'formset': formset
            }
    )


@permission_required('is_staff')
def admin_film_update_view(request, film_id):
    FilmFormSet = inlineformset_factory(
        Film, FilmImage, FilmImageForm, fields='__all__', extra=5, max_num=5)

    form = FilmForm(instance=get_film_by_id(film_id))
    formset = FilmFormSet(instance=get_film_by_id(film_id))
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES, instance=get_film_by_id(film_id))
        formset = FilmFormSet(request.POST, request.FILES, instance=get_film_by_id(film_id))
        if formset.is_valid() and form.is_valid():
            form.save()
            formset.save()
            return redirect('admin_films')

    return render(
        request,
        'admin_panel/film/film_update.html',
        {
            'film': get_film_by_id(film_id),
            'form': form,
            'formset': formset,
            'images_id': get_images_ids(get_film_by_id(film_id)),
        }
    )


@method_decorator(permission_required('is_staff'), name='dispatch')
class AdminFilmDeleteView(DeleteView):
    model = Film
    template_name = 'admin_panel/film/film_delete.html'
    success_url = reverse_lazy('admin_films')
