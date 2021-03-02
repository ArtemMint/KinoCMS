"""Schedule requests from DB
"""

from kino.models import Film
from kino.models.schedule import Schedule
from utils import get_current_date


def get_schedule_list_order_by_date_desc():
    """get schedule list by date desc from DB
    """
    return Schedule.objects.filter(
        date__gte=get_current_date()
    ).order_by('-date')


def get_schedule_list_order_by_date_asc():
    """get schedule list by date asc from DB
    """
    return Schedule.objects.filter(
        date__gte=get_current_date()
    ).order_by('date')


def get_schedule_list_order_by_current_date():
    """get schedule list by date from DB
    """
    return Schedule.objects.filter(date=get_current_date())


def get_schedule_list_for_hall_order_by_current_date(cinemahall):
    """get schedule list by current hall and date from DB
    """
    return Schedule.objects.filter(
        date=get_current_date(),
        cinemahall=cinemahall,
    )


def get_schedule_by_id(schedule_id):
    """get schedule by id DB
    """
    try:
        schedule = Schedule.objects.get(id=schedule_id)
    except Film.DoesNotExist:
        schedule = None
    return schedule
