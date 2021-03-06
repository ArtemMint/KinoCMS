from django.core.exceptions import ObjectDoesNotExist

from kino.models.news import *
from kino.models.image import NewsImage


def get_news_list():
    """get news list
    """
    try:
        news = News.objects.all()
    except ObjectDoesNotExist:
        news = None
    return news


def get_news_count():
    return get_news_list().count()


def get_news_by_id(news):
    """get news by id DB
    """
    try:
        news = News.objects.get(id=news)
    except ObjectDoesNotExist:
        news = None
    return news


def get_news_gallery(news):
    """get news gallery by id DB
    """
    try:
        gallery = NewsImage.objects.filter(news=news)
    except ObjectDoesNotExist:
        gallery = None
    return gallery