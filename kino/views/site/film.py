from django.shortcuts import render
from ...repositories.image import get_film_image_list_by_id
from ...repositories.pages import get_home_page
from ...repositories.film import get_film_by_id, get_all_films
from ...repositories.ads import *


def film_detail_view(request, film_id):
    return render(
        request,
        'kino/film_detail.html',
        {
            "film": get_film_by_id(film_id),
            "home_page": get_home_page(),
            "gallery": get_film_image_list_by_id(film_id),
            'ads':get_ads_first(),
        }
    )


def premiere_view(request):
    return render(
        request,
        'kino/premiere.html',
        {
            "film_list": get_all_films(),
            "home_page": get_home_page()
        }
    )
