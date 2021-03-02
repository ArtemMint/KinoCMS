"""Banners requests in DB"""

from django.core.exceptions import ObjectDoesNotExist

from kino.models.banners import SliderBanner, \
    SharesBanner, BackBanner


def get_slider_banners():
    """get all slider images"""
    try:
        slider_banners = SliderBanner.objects.all()
    except SliderBanner.DoesNotExist:
        slider_banners = None
    return slider_banners


def get_back_banner():
    """get background image"""
    try:
        background = BackBanner.objects.last()
    except ObjectDoesNotExist:
        background = None
    return background


def get_shares_banners():
    """get all shares images"""
    try:
        shares_banners = SharesBanner.objects.all()
    except SliderBanner.DoesNotExist:
        shares_banners = None
    return shares_banners
