from django.utils import timezone
from django.db import models
from django.urls import reverse


def upload_news_preview(instance, filename):
    return f"news/{instance.name}/preview/{filename}"


def upload_news_gallery(instance, filename):
    return f"news/{instance.name}/gallery_of_news/{filename}"


class News(models.Model):
    """Class News which using for News page

    Args:
        models (Model): [standart model]

    Returns:
        [news]: instance of News
    """

    STATUS_CHOICES = [
        ('ON', 'On'),
        ('OFF', 'Off'),
    ]

    name = models.CharField(max_length=50, default='')
    pub_date = models.DateField(editable=True, default=timezone.now)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=10, default=False, choices=STATUS_CHOICES, blank=True)
    preview = models.ImageField(upload_to=upload_news_preview, null=True)
    image1 = models.ImageField(upload_to=upload_news_gallery, blank=True, null=True)
    image2 = models.ImageField(upload_to=upload_news_gallery, blank=True, null=True)
    image3 = models.ImageField(upload_to=upload_news_gallery, blank=True, null=True)
    image4 = models.ImageField(upload_to=upload_news_gallery, blank=True, null=True)
    image5 = models.ImageField(upload_to=upload_news_gallery, blank=True, null=True)
    video = models.URLField(blank=True)
    seo_title = models.CharField(max_length=50, blank=True)
    seo_keywords = models.CharField(max_length=100, blank=True)
    seo_description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        """Func that returning name of curent news

        Returns:
            [name]: name of the news
        """
        return f"{self.name}"

    def get_absolute_url(self):
        """Func returning url needed after succeed update instance of the news

        Returns:
            [url]: page after succeed updated
        """
        return reverse("admin_news")

    def get_status(self):
        if self.status == 'ON':
            return True
        else:
            return False
