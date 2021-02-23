"""This is the ads module.

This module has ads image and url view.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.db import models

class ADS(models.Model):
    """Ads model has fields:
    image, url.
    """
    image = models.FileField(upload_to='images/ads')
    url = models.URLField()
    