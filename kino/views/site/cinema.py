from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, \
    get_object_or_404, get_list_or_404
from django.core.paginator import Paginator


from kino.models.cinema import *
from kino.models.image import CinemaImage, CinemaHallImage
from kino.models.pages import *
from ...repositories.ads import *
from ...repositories.schedule import *
from ...repositories.banners import * 


def ciname_view(request):
    cinema_list = Cinema.objects.order_by('-id')
    try:
        home_page = HomePage.objects.get(id=0)
    except HomePage.DoesNotExist:
        home_page = None

    return render(
        request,
        'kino/cinemas.html',
        {
            "cinema_list": cinema_list,
            'home_page': home_page,
            'ads': get_ads_last(),
            'background': get_back_banner(),
        },
    )


def cinema_detail_view(request, cinema_id):
    cinema = Cinema.objects.get(id=cinema_id)
    cinemahalls = CinemaHall.objects.filter(cinema=cinema).order_by('-id')
    gallery = CinemaImage.objects.filter(cinema=cinema)
    paginator = Paginator(cinemahalls, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'kino/cinema_detail.html',
        {
            'cinema': cinema,
            'cinemahalls': cinemahalls,
            'page_obj': page_obj,
            'gallery': gallery,
            'ads': get_ads_last(),
            'schedule_list': get_schedule_list_order_by_current_date(),
            'background': get_back_banner(),
        },
    )


def cinemahall_detail_view(request, cinema_id, cinemahall_id):
    cinema = get_object_or_404(Cinema, id=cinema_id)
    cinemahall = get_object_or_404(CinemaHall, id=cinemahall_id)
    gallery = CinemaHallImage.objects.filter(cinema_hall=cinemahall_id)

    return render(
        request,
        'kino/cinemahall_detail.html',
        {
            'cinema': cinema,
            'cinemahall': cinemahall,
            'gallery': gallery,
            'ads': get_ads_last(),
            'schedule_list': get_schedule_list_for_hall_order_by_current_date(cinemahall=cinemahall),
            'background': get_back_banner(),
        },
    )
