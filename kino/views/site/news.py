from django.views.generic import ListView
from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect

from kino.models.news import News


def newsView(request):
    news_list = News.objects.all()

    context = {"news_list": news_list}
    return render(request, 'kino/news.html', context)

def newsDetailView(request, news_id):
    news = get_object_or_404(News, id=news_id)

    context = {"news": news}
    return render(request, 'kino/news_detail.html', context)