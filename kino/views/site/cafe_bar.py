from django.shortcuts import redirect, render


from ...repositories.pages import *


def cafe_bar_page_view(request):
    return render(
        request, 'kino/cafe-bar.html',
        {
            'cafe_bar': get_cafe_bar_page(),
            'gallery': get_cafe_bar_image_list_by_id(4),
            'home_page': get_home_page(),
        }
    )