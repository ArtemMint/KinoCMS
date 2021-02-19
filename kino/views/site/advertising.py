from django.shortcuts import redirect, render


from ...repositories.pages import *


def advertising_page_view(request):
    return render(
        request, 'kino/advertising.html',
        {
            'advertising': get_advertising_page(),
            'gallery': get_advertising_image_list_by_id(3),
            'home_page': get_home_page(),
        }
    )
