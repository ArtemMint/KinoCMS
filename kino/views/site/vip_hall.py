"""This is the viphall module.

"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.shortcuts import redirect, render

from ...repositories.pages import *
from ...repositories.ads import *
from ...repositories.banners import * 


def vip_hall_page_view(request):
    """Vip-hall page

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """
    return render(
        request, 'kino/vip-hall.html',
        {
            'vip_hall': get_vip_hall_page(),
            'gallery': get_vip_hall_image_list_by_id(2),
            'home_page': get_home_page(),
            'ads':get_ads_last(),
            'background': get_back_banner(),
        }
    )
