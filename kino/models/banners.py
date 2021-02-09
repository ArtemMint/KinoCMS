from django.db import models
from django.core.validators import RegexValidator


class SliderBanner(models.Model):
    image = models.ImageField(blank=False, upload_to='banners/slider')
    url = models.URLField(blank=False)
    text = models.TextField(blank=True)
    # spin_speed = models.IntegerField(default=5)


class BackBanner(models.Model):
    image = models.ImageField(blank=False, upload_to='banners/back')


class SharesBanner(models.Model):
    image = models.ImageField(blank=False, upload_to='banners/shares')
    url = models.URLField(blank=False)
    # spin_speed = models.IntegerField(default=5)
