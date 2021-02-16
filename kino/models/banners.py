"""This is the banners module.

This module has banners models for database
table creating display view.
"""

__all__ = ['SliderBanner', 'BackBanner', 'SharesBanner', ]
__version__ = '0.1'
__author__ = 'Ivan Humeniuk'

from django.db import models
from django.core.validators import RegexValidator


class SliderBanner(models.Model):
    """SliderBanner model has fields:
    image, url,text.""" 
    image = models.ImageField(blank=False, upload_to='banners/slider')
    url = models.URLField(blank=False)
    text = models.TextField(blank=True)
    # spin_speed = models.IntegerField(default=5)


class BackBanner(models.Model):
    """BackBanner model has field: image.""" 
    image = models.ImageField(blank=False, upload_to='banners/back')


class SharesBanner(models.Model):
    """SharesBanner model has fields:
    image, url.""" 
    image = models.ImageField(blank=False, upload_to='banners/shares')
    url = models.URLField(blank=False)
    # spin_speed = models.IntegerField(default=5)
