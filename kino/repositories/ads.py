"""Ads requests in DB"""

from django.core.exceptions import ObjectDoesNotExist

from kino.models.ads import ADS


def get_ads_list():
    """get list of all ads"""
    try:
        ads = ADS.objects.all()
    except ObjectDoesNotExist:
        ads = None
    return ads


def get_ads_first():
    """get only first item in DB"""
    try:
        ads = ADS.objects.first()
    except ObjectDoesNotExist:
        ads = None
    return ads


def get_ads_last():
    """get only last item in DB"""
    try:
        ads = ADS.objects.last()
    except ObjectDoesNotExist:
        ads = None
    return ads
