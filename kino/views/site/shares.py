"""This is the shares module.

"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.views.generic import ListView
from django.shortcuts import get_list_or_404,\
    get_object_or_404, redirect, render

from kino.models.shares import Shares
from kino.models.image import SharesImage
from ...repositories.shares import *
from ...repositories.ads import *
from ...repositories.banners import * 


def shares_view(request):
    """Shares list

    Args:
        request ([type]): [description]

    Returns:
        [type]: [description]
    """

    return render(
        request,
        'kino/shares.html',
        {
            "shares_list": get_shares_list(),
            'ads': get_ads_last(),
            'background': get_back_banner(),
        }
    )


def shares_detail_view(request, shares_id):
    """Get one shares by id

    Args:
        request ([type]): [description]
        shares_id ([type]): [description]

    Returns:
        [type]: [description]
    """

    return render(
        request,
        'kino/shares_detail.html',
        {
            "shares": get_shares_by_id(shares_id),
            'gallery': get_shares_gallery(get_shares_by_id(shares_id)),
            'ads': get_ads_last(),
            'background': get_back_banner(),
        }
    )
