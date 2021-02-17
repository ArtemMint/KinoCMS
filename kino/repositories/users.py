from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def get_all_users_email_list() -> list or None:
    try:
        email_list = [user.email for user in User.objects.all()]
    except User.DoesNotExist:
        email_list = None

    return email_list
