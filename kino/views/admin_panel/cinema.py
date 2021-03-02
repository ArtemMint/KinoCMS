"""This is the cinema module.

This module has cinema and cinema hall views.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.urls import reverse_lazy
from django.forms import inlineformset_factory, formset_factory
from django.shortcuts import render, redirect, \
    get_object_or_404, get_list_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView

from kino.forms.cinema import *
from kino.models.cinema import *
from kino.models.image import *


# Cinema
@method_decorator(permission_required('is_staff'), name='dispatch')
class AdminCinemasView(ListView):
    """This class-based view and display 
    html template of list of cinemas."""
    model = Cinema
    template_name = 'admin_panel/cinema/cinemas.html'
    paginate_by = 4


@method_decorator(permission_required('is_staff'), name='dispatch')
class AdminCinemaDeleteView(DeleteView):
    """This class-based view and display 
    html template of delete cinema."""
    model = Cinema
    template_name = 'admin_panel/cinema/cinema_delete.html'
    success_url = reverse_lazy('admin_cinemas')


@permission_required('is_staff')
def admin_cinema_create_view(request):
    """This view which display html template of create cinema."""
    CinemaFormSet = inlineformset_factory(
        Cinema, CinemaImage, fields='__all__', extra=5, max_num=5,
    )

    form = CinemaForm()
    formset = CinemaFormSet()

    if request.method == "POST":
        form = CinemaForm(request.POST, request.FILES)
        formset = CinemaFormSet(
            request.POST, request.FILES, instance=form.instance)
        if formset.is_valid() and form.is_valid():
            form.save()
            formset.save()
            return redirect('admin_cinemas')

    return render(
        request,
        'admin_panel/cinema/cinema_add.html',
        {'form': form, 'formset': formset}
    )


@permission_required('is_staff')
def admin_cinema_update_view(request, cinema_id):
    """This view which display html template of update cinema."""
    CinemaFormSet = inlineformset_factory(
        Cinema, CinemaImage, fields='__all__', extra=5, max_num=5
    )

    cinema = Cinema.objects.get(id=cinema_id)

    form = CinemaForm(instance=cinema)
    formset = CinemaFormSet(instance=cinema)

    if request.method == "POST":
        form = CinemaForm(request.POST, request.FILES, instance=cinema)
        formset = CinemaFormSet(request.POST, request.FILES, instance=cinema)
        if formset.is_valid() and form.is_valid():
            form.save()
            formset.save()
            return redirect('admin_cinemas')

    return render(
        request,
        'admin_panel/cinema/cinema_update.html',
        {'cinema': cinema, 'form': form, 'formset': formset}
    )


@permission_required('is_staff')
def admin_cinema_detail_view(request, cinema_id):
    """This view which display html template of detail info cinema."""
    cinema = Cinema.objects.get(id=cinema_id)
    cinemahalls = CinemaHall.objects.filter(cinema=cinema).order_by('-id')
    image_list = CinemaImage.objects.filter(cinema=cinema)
    paginator = Paginator(cinemahalls, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'admin_panel/cinema/cinema_detail.html',
        {'cinema': cinema, 'cinemahalls': cinemahalls,
         'page_obj': page_obj, 'image_list': image_list}
    )


# CinemaHall
@permission_required('is_staff')
def admin_cinemahall_create_view(request, cinema_id):
    """This view which display html template of create cinema hall."""
    CinemaHallFormSet = inlineformset_factory(
        CinemaHall, CinemaHallImage, fields='__all__', extra=5, max_num=5
    )

    cinema = get_object_or_404(Cinema, id=cinema_id)

    form = CinemaHallForm()
    formset = CinemaHallFormSet(instance=form.instance)

    if request.method == "POST":
        form = CinemaHallForm(request.POST, request.FILES)
        formset = CinemaHallFormSet(
            request.POST, request.FILES, instance=form.instance)
        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            form.cinema = cinema
            form.save()
            formset.save()

            return redirect('admin_cinema_detail', cinema_id=cinema.id)

    return render(
        request,
        'admin_panel/cinema/cinemahall_add.html',
        {'form': form, 'formset': formset}
    )


@permission_required('is_staff')
def admin_cinemahall_detail_view(request, cinema_id, cinemahall_id):
    """This view which display html template of detail info cinema hall."""
    cinema = get_object_or_404(Cinema, id=cinema_id)
    cinemahall = get_object_or_404(CinemaHall, id=cinemahall_id)
    image_list = CinemaHallImage.objects.filter(cinema_hall=cinemahall)

    return render(
        request,
        'admin_panel/cinema/cinemahall_detail.html',
        {'cinema': cinema, 'cinemahall': cinemahall,
         'image_list': image_list},
    )


@permission_required('is_staff')
def admin_cinemahall_update_view(request, cinema_id, cinemahall_id):
    """This view which display html template of update cinema hall."""
    CinemaHallFormSet = inlineformset_factory(
        CinemaHall, CinemaHallImage, fields='__all__', extra=5, max_num=5
    )

    cinema = get_object_or_404(Cinema, id=cinema_id)
    cinemahall = get_object_or_404(CinemaHall, id=cinemahall_id)

    form = CinemaHallForm(instance=cinemahall)
    formset = CinemaHallFormSet(instance=cinemahall)

    if request.method == "POST":
        form = CinemaHallForm(request.POST,
                              request.FILES,
                              instance=cinemahall)
        formset = CinemaHallFormSet(
            request.POST, request.FILES, instance=cinemahall)

        if form.is_valid() and formset.is_valid():
            form = form.save(commit=False)
            form.cinema = cinema
            form.save()
            formset.save()

            return redirect('admin_cinema_detail', cinema_id=cinema.id)

    return render(
        request,
        'admin_panel/cinema/cinemahall_update.html',
        {'cinema': cinema, 'cinemahall': cinemahall,
         'form': form, 'formset': formset},
    )


@permission_required('is_staff')
def admin_cinemahall_delete_view(request, cinema_id, cinemahall_id):
    """This view which display html template of delete cinema hall."""
    cinema = get_object_or_404(Cinema, id=cinema_id)
    cinemahall = get_object_or_404(CinemaHall, id=cinemahall_id)

    if request.method == "POST":
        cinemahall.delete()

        return redirect('admin_cinema_detail', cinema_id=cinema.id)

    return render(
        request,
        'admin_panel/cinema/cinemahall_delete.html',
        {'cinema': cinema,
         'cinemahall': cinemahall},
    )
    

@require_http_methods(['GET', 'POST'])
def admin_cinemahall_type_add(request, cinema_id):
    return render(request, 'admin_panel/cinema/cinemahall_type_add.html')
