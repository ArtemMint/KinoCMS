from django.shortcuts import render

from ...repositories.banners import * 
from ...repositories.film import get_all_films
from ...repositories.pages import get_home_page
from ...repositories.ads import *


def home_page_view(request):
    return render(
        request, 'kino/home.html',
        {
            'films': get_all_films(),
            'home_page': get_home_page(),
            'background': get_back_banner(),
            'slider_banners': get_slider_banners(),
            'shares_banners': get_shares_banners(),
            'ads':get_ads_first(),
        }
    )