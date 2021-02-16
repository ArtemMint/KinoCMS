from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic import DetailView
from kino.models.film import Film
from kino.models.pages import HomePage


class FilmDetailView(DetailView):
    model = Film
    template_name = 'kino/film_detail.html'


def premiereView(request):
    film_list = Film.objects.all()
    home_page = HomePage.objects.get(id=0)

    template_name = 'kino/premiere.html'
    context = {"film_list": film_list, "home_page": home_page}
    return render(request, template_name, context)
