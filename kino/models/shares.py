from django.utils import timezone
from django.db import models
from django.urls import reverse


def upload_shares_preview(instance, filename):
    return f"shares/{instance.name}/preview/{filename}"


class Shares(models.Model):
    STATUS_CHOICES = [
        ('ON', 'On'),
        ('OFF', 'Off'),
    ]

    name = models.CharField(
        max_length=50,
        default=''
    )
    pub_date = models.DateField(
        editable=True,
        default=timezone.now
    )
    description = models.TextField(
        max_length=1000,
        blank=True
    )
    status = models.CharField(
        max_length=10,
        default=STATUS_CHOICES[1],
        choices=STATUS_CHOICES,
        blank=True
    )
    preview = models.ImageField(
        upload_to=upload_shares_preview
    )
    video = models.URLField(
        blank=True
    )
    seo_title = models.CharField(
        max_length=50,
        blank=True
    )

    seo_keywords = models.CharField(
        max_length=100,
        blank=True
    )
    seo_description = models.CharField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse("admin_shares")

    def get_status(self):
        if self.status == 'ON':
            return True
        else:
            return False
