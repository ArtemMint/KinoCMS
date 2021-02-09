from django.views.generic import ListView, DetailView
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator


from kino.models.cinema import Cinema, CinemaHall


class CinemasView(ListView):
    model = Cinema
    template_name = 'kino/cinemas.html'


def cinemaDetailView(request, cinema_id):
    cinema = get_object_or_404(Cinema, id=cinema_id)
    cinemahalls = get_list_or_404(
        CinemaHall.objects.order_by('-id'), cinema=cinema)
    paginator = Paginator(cinemahalls, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'cinema': cinema,
               'cinemahalls': cinemahalls, 'page_obj': page_obj}
    return render(request, 'kino/cinema_detail.html', context)


def cinemahallDetailView(request, cinema_id, cinemahall_id):
    cinema = get_object_or_404(Cinema, id=cinema_id)
    cinemahall = get_object_or_404(CinemaHall, id=cinemahall_id)
    context = {'cinema': cinema,
               'cinemahall': cinemahall}
    return render(request, 'kino/cinemahall_detail.html', context)
