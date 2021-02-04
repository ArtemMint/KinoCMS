from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from kino.models.news import News
from kino.forms.news import NewsForm


class AdminNewsView(ListView):
    model = News
    template_name = 'admin_panel/news/news.html'
    ordering = ['-id']


class AdminNewsDetailView(DetailView):
    model = News
    template_name = 'admin_panel/news/news_detail.html'


class AdminNewsAddView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'admin_panel/news/news_add.html'


class AdminNewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'admin_panel/news/news_update.html'


class AdminNewsDeleteView(DeleteView):
    model = News
    template_name = 'admin_panel/news/news_delete.html'
    success_url = reverse_lazy('admin_news')