from kino.forms.banners import *
from django.core.handlers.wsgi import WSGIRequest
from django.forms.models import ModelFormMetaclass


def banners_slider_form_save(request):
    counter = 0
    for file in request.FILES.getlist('slider_banner_image'):
        form = SliderBannerForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            [obj.image, obj.url, obj.text] = [file, request.POST.getlist('url')[counter],
                                              request.POST.getlist('text')[counter]]
            obj.save()
        counter += 1


def get_instance_from_request_query_list(query_set, field: str, index: int):
    return query_set.getlist(field)[index]


def banners_form_list(request: WSGIRequest, form: ModelFormMetaclass) -> list:
    return [form(request.POST or None, instance=None) for i in range(5)]
