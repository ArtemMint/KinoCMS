"""User mailing"""

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def get_all_users_email_list():
    """Get e-mail from all existing users"""
    try:
        email_list = [
            user.email for user in User.objects.all()
        ]
    except ObjectDoesNotExist:
        email_list = None

    return email_list
