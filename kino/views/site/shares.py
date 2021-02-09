from django.views.generic import ListView
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render

from kino.models.shares import Shares


def sharesView(request):
    shares_list = get_list_or_404(Shares)

    context = {"shares_list": shares_list}
    return render(request, 'kino/shares.html', context)


def sharesDetailView(request, shares_id):
    shares = get_object_or_404(Shares, id=shares_id)

    context = {"shares": shares}
    return render(request,'kino/shares_detail.html', context)
