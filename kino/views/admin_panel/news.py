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


@method_decorator(permission_required('is_staff'), name='dispatch')
class AdminNewsView(ListView):
    model = News
    template_name = 'admin_panel/news/news.html'
    ordering = ['-id']
    paginate_by = 15


@permission_required('is_staff')
def admin_news_detail_view(request, news_id):
    news = News.objects.get(id=news_id)
    image_list = NewsImage.objects.filter(news=news)

    template_name = 'admin_panel/news/news_detail.html'
    context = {'news': news, 'image_list': image_list}
    return render(request, template_name, context)


@permission_required('is_staff')
def admin_news_create_view(request):
    NewsFormSet = inlineformset_factory(
        News, NewsImage, fields='__all__', extra=5, max_num=5)

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

    template_name = 'admin_panel/news/news_add.html'
    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


@permission_required('is_staff')
def admin_news_update_view(request, news_id):
    NewsFormSet = inlineformset_factory(
        News, NewsImage, fields='__all__', extra=5, max_num=5)
    news = News.objects.get(id=news_id)
    form = NewsForm(instance=news)
    formset = NewsFormSet(instance=news)

    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news)
        formset = NewsFormSet(
            request.POST, request.FILES, instance=news)
        if formset.is_valid() and form.is_valid():
            form.save()
            formset.save()
            return redirect('admin_news')

    template_name = 'admin_panel/news/news_update.html'
    context = {'news': news, 'form': form, 'formset': formset}
    return render(request, template_name, context)


@method_decorator(permission_required('is_staff'), name='dispatch')
class AdminNewsDeleteView(DeleteView):
    model = News
    template_name = 'admin_panel/news/news_delete.html'
    success_url = reverse_lazy('admin_news')
