from kino.models import Film
from kino.models.schedule import Schedule
from utils import get_current_date


def get_schedule_list_order_by_date_desc():
    return Schedule.objects.filter(
        date__gte=get_current_date()
    ).order_by('-date')


def get_schedule_list_order_by_date_asc():
    return Schedule.objects.filter(
        date__gte=get_current_date()
    ).order_by('date')


def get_schedule_list_order_by_current_date():
    return Schedule.objects.filter(date=get_current_date())


def get_schedule_list_for_hall_order_by_current_date(cinemahall):
    return Schedule.objects.filter(
        date=get_current_date(),
        cinemahall=cinemahall,
    )


def get_schedule_by_id(schedule_id):
    try:
        schedule = Schedule.objects.get(id=schedule_id)
    except Film.DoesNotExist:
        schedule = None
    return schedule
