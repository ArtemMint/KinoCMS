from django.views.generic import ListView

from kino.models.news import News


class NewsView(ListView):
    model = News
    template_name = 'kino/news.html'



