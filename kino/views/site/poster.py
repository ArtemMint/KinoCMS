from django.shortcuts import render, redirect, \
    get_object_or_404, get_list_or_404

from kino.models.film import Film
from kino.models.pages import HomePage
from ...repositories.ads import *


def poster_view(request):
    film_list = Film.objects.all()
    try:
        home_page = HomePage.objects.get(id=0)
    except HomePage.DoesNotExist:
        home_page = None

    return render(
        request,
        'kino/poster.html',
        {
            "film_list": film_list,
            "home_page": home_page,
            'ads':get_ads_last(),
        }
    )
