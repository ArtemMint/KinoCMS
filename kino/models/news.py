from django.utils import timezone
from django.db import models
from django.urls import reverse


def upload_news_preview(instance, filename):
    return f"news/{instance.name}/preview/{filename}"


def upload_news_gallery(instance, filename):
    return f"news/{instance.name}/gallery_of_news/{filename}"


class News(models.Model):
    """Class News which using for News pageW"""

    STATUS_CHOICES = [
        ('ON', 'On'),
        ('OFF', 'Off'),
    ]

    name = models.CharField(max_length=50, default='')
    pub_date = models.DateField(editable=True, default=timezone.now)
    description = models.TextField()
    status = models.CharField(
        max_length=10, default=STATUS_CHOICES[1], choices=STATUS_CHOICES
    )
    preview = models.ImageField(upload_to=upload_news_preview, null=True)
    video = models.URLField(blank=True)
    seo_title = models.CharField(max_length=50, blank=True)
    seo_keywords = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        """Func that returning name of curent news"""
        return f"{self.name}"

    def get_absolute_url(self):
        """Func returning url needed 
        after succeed update instance of the news
        """
        return reverse("admin_news")

    def get_status(self):
        if self.status == 'ON':
            return True
        else:
            return False
