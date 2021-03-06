from django.shortcuts import redirect, render

from ...repositories.pages import *
from ...repositories.ads import *
from ...repositories.banners import * 


def children_room_page_view(request):
    return render(
        request, 'kino/children-room.html',
        {
            'children_room': get_children_room_page(),
            'gallery': get_children_room_image_list_by_id(4),
            'home_page': get_home_page(),
            'ads':get_ads_last(),
            'background': get_back_banner(),
        }
    )
