from django.utils import timezone
from django.db import models
from.shares import upload_shares_gallery, upload_shares_preview


class PageModel(models.Model):
    name = models.CharField(max_length=50, default='')
    pub_date = models.DateField(default=timezone.now)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    preview = models.ImageField(upload_to=upload_shares_preview)
    image1 = models.ImageField(upload_to=upload_shares_gallery, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_shares_gallery, blank=True, null=True)
    image3 = models.ImageField(upload_to=upload_shares_gallery, blank=True, null=True)
    image4 = models.ImageField(upload_to=upload_shares_gallery, blank=True, null=True)
    image5 = models.ImageField(upload_to=upload_shares_gallery, blank=True, null=True)
    seo_title = models.CharField(max_length=50, blank=True)
    seo_keywords = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.name}'


class HomePageModel(models.Model):
    page = models.OneToOneField(PageModel, on_delete=models.CASCADE)
    phone1 = models.CharField(max_length=14, blank=True, null=True)
    phone2 = models.CharField(max_length=14, blank=True, null=True)

    def __str__(self):
        return f'{self.page.name}'


class ContactModel(models.Model):
    name = models.CharField(max_length=50, default='')
    pub_date = models.DateField(default=timezone.now)
    address = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    latitude = models.FloatField(max_length=50)
    longitude = models.FloatField(max_length=50)
    logo = models.ImageField(upload_to=upload_shares_preview)
    seo_title = models.CharField(max_length=50, blank=True)
    seo_keywords = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.name}'