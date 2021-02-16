from django.views.generic import ListView
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render

from kino.models.shares import Shares
from kino.models.image import SharesImage


def shares_view(request):
    shares_list = Shares.objects.all()

    context = {"shares_list": shares_list}
    return render(request, 'kino/shares.html', context)


def shares_detail_view(request, shares_id):
    shares = get_object_or_404(Shares, id=shares_id)
    gallery = SharesImage.objects.filter(shares=shares)

    template_name = 'kino/shares_detail.html'
    context = {"shares": shares, gallery: gallery}

    return render(request, template_name, context)
