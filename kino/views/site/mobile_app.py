from django.shortcuts import redirect, render


from ...repositories.pages import *
from ...repositories.ads import *


def mobile_app_page_view(request):
    return render(
        request, 'kino/mobile_app.html',
        {
            'mobile_app': get_mobile_app_page(),
            'gallery': get_mobile_app_image_list_by_id(5),
            'home_page': get_home_page(),
            'ads':get_ads_last(),
        }
    )
