from django.core.exceptions import ObjectDoesNotExist

from kino.models.cinema import *
from kino.models.image import *


def get_cinema_list():
    """get cinema list
    """
    try:
        cinema = Cinema.objects.all()
    except ObjectDoesNotExist:
        cinema = None
    return cinema


def get_cinema_count():
    return get_cinema_list().count()


def get_cinema_by_id(cinema):
    """get one cinema by id
    """
    try:
        cinema = Cinema.objects.get(id=cinema)
    except ObjectDoesNotExist:
        cinema = None
    return cinema


def get_cinemahall_list(cinema):
    """get cinemahall list
    """
    try:
        cinemahall = CinemaHall.objects.filter(
            cinema=cinema
            ).order_by('-id')
    except ObjectDoesNotExist:
        cinemahall = None
    return cinemahall


def get_cinemahall_by_id(cinema):
    """get one cinemahall by id
    """
    try:
        cinemahall = CinemaHall.objects.get(cinema=cinema)
    except ObjectDoesNotExist:
        cinemahall = None
    return cinemahall


def get_cinema_gallery(cinema):
    """get one cinemahall by id
    """
    try:
        cinema_gallery = CinemaImage.objects.filter(cinema=cinema)
    except ObjectDoesNotExist:
        cinema_gallery = None
    return cinema_gallery


def get_cinemahall_gallery(cinemahall):
    """get one cinemahall by id
    """
    try:
        cinemahall_gallery = CinemaHallImage.objects.filter(cinema_hall=cinemahall)
    except ObjectDoesNotExist:
        cinemahall_gallery = None
    return cinemahall_gallery
