from django.shortcuts import redirect, render


from ...repositories.pages import *


def vip_hall_page_view(request):
    return render(
        request, 'kino/vip-hall.html',
        {
            'vip_hall': get_vip_hall_page(),
            'gallery': get_vip_hall_image_list_by_id(2),
            'home_page': get_home_page(),
        }
    )
