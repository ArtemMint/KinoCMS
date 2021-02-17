from django.views.generic import ListView
from django.shortcuts import get_object_or_404, \
    get_list_or_404, render, redirect

from kino.models.news import News
from kino.models.image import NewsImage


def news_view(request):
    news_list = News.objects.all()

    template_name = 'kino/news.html'
    context = {"news_list": news_list}

    return render(request, template_name, context)


def news_detail_view(request, news_id):
    news = News.objects.get(id=news_id)
    gallery = NewsImage.objects.filter(news=news)

    template_name = 'kino/news_detail.html'
    context = {"news": news, 'gallery': gallery}

    return render(request, template_name, context)
