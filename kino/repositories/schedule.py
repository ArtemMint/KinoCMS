from kino.models.schedule import Schedule


def get_schedule_list() -> list:
    return Schedule.objects.all().order_by('-date')


def get_schedule_by_id(schedule_id) -> Schedule or None:
    try:
        schedule = Schedule.objects.get(id=schedule_id)
    except Film.DoesNotExist:
        schedule = None
    return schedule
