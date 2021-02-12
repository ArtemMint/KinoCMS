from django.utils import timezone
from django.db import models
from .shares import upload_shares_gallery, upload_shares_preview
from phonenumber_field.modelfields import PhoneNumberField

# class Client(models.Model, Importable):
#     phone = PhoneNumberField(null=False, blank=False, unique=True)


class HomePage(models.Model):
    phone1 = PhoneNumberField(null=False, blank=False, unique=True)
    phone2 = PhoneNumberField(null=False, blank=False, unique=True)
    seo_text = models.TextField(max_length=500)
    seo_title = models.CharField(max_length=50, blank=True)
    seo_keywords = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.pk}'


class Contacts(models.Model):
    name = models.CharField(max_length=50, default='')
    address = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    coordinates = models.CharField(max_length=50)
    logo = models.ImageField(upload_to=upload_shares_preview)
    seo_title = models.CharField(max_length=50, blank=True)
    seo_keywords = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.name}'


class Page(models.Model):
    name = models.CharField(max_length=50, default='')
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    preview = models.ImageField(upload_to=upload_shares_preview)
    image1 = models.ImageField(
        upload_to=upload_shares_gallery, blank=True, null=True)
    image2 = models.ImageField(
        upload_to=upload_shares_gallery, blank=True, null=True)
    image3 = models.ImageField(
        upload_to=upload_shares_gallery, blank=True, null=True)
    image4 = models.ImageField(
        upload_to=upload_shares_gallery, blank=True, null=True)
    image5 = models.ImageField(
        upload_to=upload_shares_gallery, blank=True, null=True)
    seo_title = models.CharField(max_length=50, blank=True)
    seo_keywords = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.name}'
