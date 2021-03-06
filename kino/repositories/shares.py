"""Shares requests in DB"""

from django.core.exceptions import ObjectDoesNotExist

from kino.models.shares import Shares
from kino.models.image import SharesImage


def get_shares_list():
    """Get list of shares"""
    try:
        shares = Shares.objects.all()
    except ObjectDoesNotExist:
        shares = None
    return shares


def get_shares_count():
    return get_shares_list().count()


def get_shares_gallery(shares):
    """Get list of shares"""
    try:
        shares = SharesImage.objects.filter(shares=shares)
    except ObjectDoesNotExist:
        shares = None
    return shares


def get_shares_by_id(shares):
    """Get list of shares"""
    try:
        shares = Shares.objects.get(id=shares)
    except ObjectDoesNotExist:
        shares = None
    return shares
