from django.views.generic import ListView
from django.shortcuts import get_list_or_404,\
    get_object_or_404, redirect, render

from kino.models.shares import Shares
from kino.models.image import SharesImage
from ...repositories.ads import *
from ...repositories.banners import * 


def shares_view(request):
    shares_list = Shares.objects.all()

    return render(
        request,
        'kino/shares.html',
        {
            "shares_list": shares_list,
            'ads': get_ads_last(),
            'background': get_back_banner(),
        }
    )


def shares_detail_view(request, shares_id):
    shares = get_object_or_404(Shares, id=shares_id)
    gallery = SharesImage.objects.filter(shares=shares)

    return render(
        request,
        'kino/shares_detail.html',
        {
            "shares": shares,
            'gallery': gallery,
            'ads': get_ads_last(),
            'background': get_back_banner(),
        }
    )
