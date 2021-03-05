from django.urls import reverse_lazy
from django.shortcuts import render, \
    redirect, get_object_or_404, get_list_or_404
from django.views.generic import ListView, \
    DetailView, CreateView, UpdateView, DeleteView
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator

from kino.models.news import News
from kino.forms.news import NewsForm
from kino.models.image import NewsImage
from ...repositories.news import *


@method_decorator(permission_required('is_staff'), name='dispatch')
class AdminNewsView(ListView):
    model = News
    template_name = 'admin_panel/news/news.html'
    ordering = ['-id']
    paginate_by = 15


@permission_required('is_staff')
def admin_news_detail_view(request, news_id):
    return render(
        request,
        'admin_panel/news/news_detail.html',
        {
            'news': get_news_by_id(news_id),
            'image_list': get_news_gallery(get_news_by_id(news_id)),
        }
    )


@permission_required('is_staff')
def admin_news_create_view(request):
    NewsFormSet = inlineformset_factory(
        News,
        NewsImage,
        fields='__all__',
        extra=5,
        max_num=5,
    )

    form = NewsForm()
    formset = NewsFormSet()

    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        formset = NewsFormSet(
            request.POST, request.FILES, instance=form.instance)
        if formset.is_valid() and form.is_valid():
            form.save()
            formset.save()
            return redirect('admin_news')

    return render(
        request,
        'admin_panel/news/news_add.html',
        {
            'form': form,
            'formset': formset
        }
    )


@permission_required('is_staff')
def admin_news_update_view(request, news_id):
    NewsFormSet = inlineformset_factory(
        News,
        NewsImage,
        fields='__all__',
        extra=5,
        max_num=5,
    )
    form = NewsForm(instance=get_news_by_id(news_id))
    formset = NewsFormSet(instance=get_news_by_id(news_id))

    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=get_news_by_id(news_id))
        formset = NewsFormSet(
            request.POST, request.FILES, instance=get_news_by_id(news_id))
        if formset.is_valid() and form.is_valid():
            form.save()
            formset.save()
            return redirect('admin_news')

    return render(
        request,
        'admin_panel/news/news_update.html',
        {
            'news': get_news_by_id(news_id),
            'form': form,
            'formset': formset,
        }
    )


@method_decorator(permission_required('is_staff'), name='dispatch')
class AdminNewsDeleteView(DeleteView):
    model = News
    template_name = 'admin_panel/news/news_delete.html'
    success_url = reverse_lazy('admin_news')
