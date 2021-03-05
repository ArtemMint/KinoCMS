from django.shortcuts import redirect, render

from ...repositories.pages import get_home_page
from ...repositories.schedule import *
from ...repositories.ads import *
from ...repositories.banners import * 


def schedule_page_view(request):
    return render(
        request, 'kino/schedule.html',
        {
            'schedule_list': get_schedule_list_order_by_date_asc(),
            'home_page': get_home_page(),
            'ads':get_ads_last(),
            'background': get_back_banner(),
        }
    )
