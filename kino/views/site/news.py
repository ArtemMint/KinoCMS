from django.views.generic import ListView
from django.shortcuts import get_object_or_404, \
    get_list_or_404, render, redirect

from kino.models.news import News
from kino.models.image import NewsImage
from ...repositories.ads import *
from ...repositories.banners import *


def news_view(request):
    news_list = News.objects.all()

    return render(
        request,
        'kino/news.html',
        {
            "news_list": news_list,
            'ads': get_ads_last(),
            'background': get_back_banner(),
        }
    )


def news_detail_view(request, news_id):
    news = News.objects.get(id=news_id)
    gallery = NewsImage.objects.filter(news=news)

    return render(
        request,
        'kino/news_detail.html',
        {
            "news": news,
            'gallery': gallery,
            'ads': get_ads_last(),
            'background': get_back_banner(),
        }
    )
