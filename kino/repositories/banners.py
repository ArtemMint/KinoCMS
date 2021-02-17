from ..models.banners import *


def get_slider_banners():
    try:
        slider_banners = SliderBanner.objects.all()[::-1][:5]
    except SliderBanner.DoesNotExist:
        slider_banners = None
    print([banner.image for banner in slider_banners])
    return slider_banners


def get_back_banner() -> list:
    pass


def get_shares_banners() -> list:
    try:
        shares_banners = SharesBanner.objects.all()[::-1][:5]
    except SliderBanner.DoesNotExist:
        shares_banners = None
    print(shares_banners)
    return shares_banners
