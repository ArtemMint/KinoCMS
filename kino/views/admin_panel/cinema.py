from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from kino.forms.cinema import CinemaForm, CinemaHallForm
from kino.models.cinema import Cinema, CinemaHall


class AdminCinemasView(ListView):
    model = Cinema
    template_name = 'admin_panel/cinema/cinemas.html'


def adminCinemaDetailView(request, cinema_id):
    cinema = get_object_or_404(Cinema, id=cinema_id)
    cinemahalls = get_list_or_404(CinemaHall.objects.order_by('-id'), cinema=cinema)
    paginator = Paginator(cinemahalls, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'cinema': cinema, 'cinemahalls': cinemahalls, 'page_obj': page_obj}
    return render(request, 'admin_panel/cinema/cinema_detail.html', context)


def adminCinemahallCreateView(request, cinema_id):
    cinema = get_object_or_404(Cinema, id=cinema_id)
    if request.method == "POST":
        form = CinemaHallForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.cinema = cinema
            form.save()
            return redirect('admin_cinema_detail', cinema_id=cinema.id)
    else:
        form = CinemaHallForm()
    return render(
        request,
        'admin_panel/cinema/cinemahall_add.html',
        {'cinemahall_form': form})


def adminCinemahallDetailView(request, cinema_id, cinemahall_id):
    """
    Detail view for Hall of the Cinema
    """
    cinema = get_object_or_404(Cinema, id=cinema_id)
    cinemahall = get_object_or_404(CinemaHall, id=cinemahall_id)
    context = {'cinema': cinema, 'cinemahall': cinemahall}
    return render(request, 'admin_panel/cinema/cinemahall_detail.html', context)


def adminCinemahallUpdateView(request, cinema_id, cinemahall_id):
    """
    Edit Hall in the Cinema
    """
    cinema = get_object_or_404(Cinema, id=cinema_id)
    cinemahall = get_object_or_404(CinemaHall, id=cinemahall_id)
    form = CinemaHallForm(instance=cinemahall)

    if request.method == "POST":
        form = CinemaHallForm(request.POST, instance=cinemahall)
        if form.is_valid():
            form.save()
            return redirect('admin_cinema_detail', cinema_id=cinema.id)
    context = {'cinema': cinema,
               'cinemahall': cinemahall, 'cinemahall_form': form}
    return render(
        request,
        'admin_panel/cinema/cinemahall_update.html', context
    )


def adminCinemahallDeleteView(request, cinema_id, cinemahall_id):
    """
    Delete Hall in the Cinema
    """
    cinema = get_object_or_404(Cinema, id=cinema_id)
    cinemahall = get_object_or_404(CinemaHall, id=cinemahall_id)

    if request.method == "POST":
        cinemahall.delete()
        return redirect('admin_cinema_detail', cinema_id=cinema.id)
    context = {'cinema': cinema,
               'cinemahall': cinemahall}
    return render(
        request,
        'admin_panel/cinema/cinemahall_delete.html', context
    )


class AdminCinemahallUpdateView(UpdateView):
    model = CinemaHall
    form_class = CinemaHallForm
    template_name = 'admin_panel/cinema/cinemahall_update.html'


class AdminCinemahallDeleteView(DeleteView):
    model = CinemaHall
    template_name = 'admin_panel/cinema/cinemahall_delete.html'
    success_url = reverse_lazy('admin_cinemas')


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
