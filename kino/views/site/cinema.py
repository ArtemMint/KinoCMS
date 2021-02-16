from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, \
    get_object_or_404, get_list_or_404
from django.core.paginator import Paginator


from kino.models.cinema import *
from kino.models.image import CinemaImage, CinemaHallImage
from kino.models.pages import *


def ciname_view(request):
    cinema_list = Cinema.objects.order_by('-id')
    home_page = HomePage.objects.get(id=0)

    context = {"cinema_list": cinema_list, 'home_page': home_page}
    template_name = 'kino/cinemas.html'

    return render(request, template_name, context)


def cinema_detail_view(request, cinema_id):
    cinema = Cinema.objects.get(id=cinema_id)
    cinemahalls = CinemaHall.objects.filter(cinema=cinema).order_by('-id')
    gallery = CinemaImage.objects.filter(cinema=cinema)
    paginator = Paginator(cinemahalls, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    template_name = 'kino/cinema_detail.html'
    context = {'cinema': cinema, 'cinemahalls': cinemahalls,
               'page_obj': page_obj, 'gallery': gallery}

    return render(request, template_name, context)


def cinemahall_detail_view(request, cinema_id, cinemahall_id):
    cinema = get_object_or_404(Cinema, id=cinema_id)
    cinemahall = get_object_or_404(CinemaHall, id=cinemahall_id)
    gallery = CinemaImage.objects.filter(cinema=cinemahall_id)

    template_name = 'kino/cinemahall_detail.html'
    context = {'cinema': cinema,'cinemahall': cinemahall, 'gallery': gallery}
    return render(request, template_name, context)
