from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from kino.forms.film import FilmForm
from kino.models.film import Film
from kino.models.image import FilmImage
from ...repositories.film import get_film_by_id
from ...repositories.image import get_film_image_list_by_id


class AdminFilmsView(ListView):
    model = Film
    template_name = 'admin_panel/film/films.html'
    ordering = ['-id']
    paginate_by = 15


def admin_film_detail_view(request, film_id):
    return render(
        request,
        'admin_panel/film/film_detail.html',
        {
            'film': get_film_by_id(film_id),
            'image_list': get_film_image_list_by_id(film_id)
        }
    )


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

    template_name = 'admin_panel/film/film_add.html'
    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


def admin_film_update_view(request, film_id):
    FilmFormSet = inlineformset_factory(
        Film, FilmImage, fields='__all__', extra=5, max_num=5)
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
    context = {'film': film, 'form': form, 'formset': formset}

    return render(request, template_name, context)


class AdminFilmDeleteView(DeleteView):
    model = Film
    template_name = 'admin_panel/film/film_delete.html'
    success_url = reverse_lazy('admin_films')
