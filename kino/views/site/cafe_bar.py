from django.shortcuts import render

from ...repositories.pages import *
from ...repositories.ads import *
from ...repositories.banners import * 


def cafe_bar_page_view(request):
    return render(
        request, 'kino/cafe-bar.html',
        {
            'cafe_bar': get_cafe_bar_page(),
            'gallery': get_cafe_bar_image_list_by_id(1),
            'home_page': get_home_page(),
            'ads': get_ads_last(),
            'background': get_back_banner(),
        }
    )
