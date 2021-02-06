from django.urls import reverse_lazy
from django.http import Http404
from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from kino.forms.cinema import CinemaForm, CinemaHallForm
from kino.models.cinema import Cinema, CinemaHall


class AdminCinemasView(ListView):
    model = Cinema
    template_name = 'admin_panel/cinema/cinemas.html'


def adminCinemaDetailView(request, cinema_id):
    try:
        cinema = Cinema.objects.get(id=cinema_id)
        cinemahalls = CinemaHall.objects.filter(cinema=cinema)
    except cinema.DoesNotExist:
        raise Http404("Cinema does not exist")
    context = {'cinema': cinema, 'cinemahalls': cinemahalls}
    return render(request, 'admin_panel/cinema/cinema_detail.html', context)


def adminNewCinemahallView(request, cinema_id):
    try:
        cinema = Cinema.objects.get(pk=cinema_id)
    except cinema.DoesNotExist:
        raise Http404("Cinema does not exist")

    if request.method == "POST":
        form = CinemaHallForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.cinema = cinema
            form.save()
            return redirect('admin_cinemas')
    else:
        form = CinemaHallForm()
    return render(
        request,
        'admin_panel/cinema/cinemahall_add.html',
        {'cinemahall_form': form})


class AdminCinemaAddView(CreateView):
    model = Cinema
    form_class = CinemaForm
    template_name = 'admin_panel/cinema/cinema_add.html'


class AdminCinemaUpdateView(UpdateView):
    model = Cinema
    form_class = CinemaForm
    template_name = 'admin_panel/cinema/cinema_update.html'


class AdminCinemaDeleteView(DeleteView):
    model = Cinema
    template_name = 'admin_panel/cinema/cinema_delete.html'
    success_url = reverse_lazy('admin_cinemas')
