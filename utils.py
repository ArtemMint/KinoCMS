import datetime

from django.utils import timezone


def current_year():
    return datetime.datetime.now().year


def get_current_date():
    return timezone.now()


def get_avg_age(set_of_users):
    avg_age = 0
    if not set_of_users:
        return 0
    else:
        for user in set_of_users:
            if user.birth_date is None:
                pass
            else:
                avg_age = avg_age + user.get_age()

        return avg_age // set_of_users.count()
