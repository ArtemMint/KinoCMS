from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.forms import inlineformset_factory
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from kino.forms.cinema import CinemaForm, CinemaHallForm
from kino.models.cinema import Cinema, CinemaHall
from kino.models.image import CinemaImage


class AdminCinemasView(ListView):
    model = Cinema
    template_name = 'admin_panel/cinema/cinemas.html'


def admin_cinema_add_view(request):
    CinemaFormSet = inlineformset_factory(
        Cinema, CinemaImage, fields='__all__', extra=5, max_num=5)

    form = CinemaForm()
    formset = CinemaFormSet()

    if request.method == "POST":
        form = CinemaForm(request.POST, request.FILES)
        formset = CinemaFormSet(request.POST, request.FILES)
        if formset.is_valid() and form.is_valid():
            form.save()
            formset.save()
            return redirect('admin_cinemas')

    template_name = 'admin_panel/cinema/cinema_add.html'
    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


def admin_cinema_update_view(request, cinema_id):
    CinemaFormSet = inlineformset_factory(
        Cinema, CinemaImage, fields='__all__', extra=5, max_num=5)
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

    template_name = 'admin_panel/cinema/cinema_update.html'
    context = {'cinema': cinema, 'form': form, 'formset': formset}
    return render(request, template_name, context)


def admin_cinema_detail_view(request, cinema_id):
    cinema = Cinema.objects.get(id=cinema_id)
    cinemahalls = CinemaHall.objects.filter(cinema=cinema).order_by('-id')
    image_list = CinemaImage.objects.filter(cinema=cinema)
    paginator = Paginator(cinemahalls, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'cinema': cinema, 'cinemahalls': cinemahalls,
               'page_obj': page_obj, 'image_list': image_list}
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

    if request.method == "POST":
        form = CinemaHallForm(request.POST, instance=cinemahall)
        if form.is_valid():
            form.save()
            return redirect('admin_cinema_detail', cinema_id=cinema.id)
    else:
        form = CinemaHallForm(instance=cinemahall)
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


class AdminCinemaDeleteView(DeleteView):
    model = Cinema
    template_name = 'admin_panel/cinema/cinema_delete.html'
    success_url = reverse_lazy('admin_cinemas')
