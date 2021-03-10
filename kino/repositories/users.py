"""User mailing"""

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from register.models.client import Client
from utils import get_avg_age


def get_users_list():
    try:
        users_list = Client.objects.all()
    except ObjectDoesNotExist:
        users_list = ''
    return users_list


def get_users_count():
    try:
        users_count = Client.objects.all().count()
    except ObjectDoesNotExist:
        users_count = ''
    return users_count
    

def get_users_avg_age():
    return get_avg_age(get_users_list())


def get_men_list():
    try:
        men_list = Client.objects.filter(gender='Male')
    except ObjectDoesNotExist:
        men_list = ''
    return men_list


def get_men_count():
    return get_men_list().count()


def get_men_avg_age():
    return get_avg_age(get_men_list())


def get_women_list():
    try:
        women_list = Client.objects.filter(gender='Female')
    except ObjectDoesNotExist:
        women_list = ''
    return women_list


def get_women_count():
    return get_women_list().count()


def get_women_avg_age():
    return get_avg_age(get_women_list())


def get_all_users_email_list():
    """Get e-mail from all existing users"""
    try:
        email_list = [
            user.email for user in User.objects.all()
        ]
    except ObjectDoesNotExist:
        email_list = None

    return email_list
