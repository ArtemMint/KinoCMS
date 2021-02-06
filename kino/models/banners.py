from django.db import models
from django.core.validators import RegexValidator


class BackBanner(models.Model):
    image = models.ImageField(blank=False, upload_to='')


class SharesBanner(models.Model):
    image = models.ImageField(blank=False, upload_to='')
    url = models.URLField(blank=False)
    spin_speed = models.IntegerField(default=5)


class SpinnerBanner(models.Model):
    image = models.ImageField(blank=False, upload_to='')
    url = models.URLField(blank=False)
    text = models.TextField(max_length=2000,
                            validators=RegexValidator(regex=r'', message=''))
    spin_speed = models.IntegerField(default=5)

# TODO add RegexValidator
