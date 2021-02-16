from django.shortcuts import render, redirect, \
    get_object_or_404, get_list_or_404

from kino.models.film import Film
from kino.models.pages import HomePage


def poster_view(request):
    film_list = Film.objects.all()
    home_page = HomePage.objects.get(id=0)

    template_name = 'kino/poster.html'
    context = {"film_list": film_list, "home_page": home_page}
    return render(request, template_name, context)
