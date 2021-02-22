from kino.models.schedule import Schedule
from utils import get_current_date


def get_schedule_list_order_by_date_desc() -> list:
    return Schedule.objects.filter(date__gte=get_current_date()).order_by('-date')


def get_schedule_list_order_by_date_asc() -> list:
    return Schedule.objects.filter(date__gte=get_current_date()).order_by('date')


def get_schedule_by_id(schedule_id) -> Schedule or None:
    try:
        schedule = Schedule.objects.get(id=schedule_id)
    except Film.DoesNotExist:
        schedule = None
    return schedule
