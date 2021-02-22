from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import DeleteView

from kino.models.film import Film
from kino.models.cinema import CinemaHall
from kino.forms.schedule import ScheduleForm
from ...repositories.schedule import *

def admin_schedule_view(request):
    return render(
        request,
        'admin_panel/schedule/schedule.html',
        {
            'schedule_list': get_schedule_list_order_by_date_asc(),
        }
    )


def admin_schedule_create_view(request):

    form = ScheduleForm()
    if request.method == "POST":
        form = ScheduleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_schedule')

    return render(
        request,
        'admin_panel/schedule/schedule_add.html',
        {'form': form,}
    )


def admin_schedule_update_view(request, schedule_id):

    form = ScheduleForm(instance=get_schedule_by_id(schedule_id))
    if request.method == "POST":
        form = ScheduleForm(request.POST, request.FILES, instance=get_schedule_by_id(schedule_id))
        if form.is_valid():
            form.save()
            return redirect('admin_schedule')

    return render(
        request,
        'admin_panel/schedule/schedule_update.html',
        {
            'schedule': get_schedule_by_id(schedule_id),
            'form': form,
        }
    )


class AdminScheduleDeleteView(DeleteView):
    model = Schedule
    template_name = 'admin_panel/schedule/schedule_delete.html'
    success_url = reverse_lazy('admin_schedule')
