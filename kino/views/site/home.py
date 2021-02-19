from django.shortcuts import render
from ...repositories.film import get_all_films
from ...repositories.pages import get_home_page
from ...repositories.banners import get_slider_banners, get_shares_banners


def home_page_view(request):
    return render(
        request, 'kino/home.html',
        {
            'films': get_all_films(),
            'home_page': get_home_page(),
            'slider_banners': get_slider_banners(),
            'shares_banners': get_shares_banners()
        }
    )
