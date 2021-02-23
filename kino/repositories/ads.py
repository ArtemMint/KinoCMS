from django.core.exceptions import ObjectDoesNotExist

from kino.models.ads import ADS


def get_ads_list() -> ADS:
    try:
        ads = ADS.objects.all()
    except ObjectDoesNotExist:
        ads = None
    return ads


def get_ads_first() -> ADS:
    try:
        ads = ADS.objects.first()
    except ObjectDoesNotExist:
        ads = None
    return ads


def get_ads_last() -> ADS:
    try:
        ads = ADS.objects.last()
    except ObjectDoesNotExist:
        ads = None
    return ads