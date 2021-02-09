from kino.models.banners import *
from kino.forms.banners import *
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render, reverse
from kino.services.banners import banners_form_list


@require_http_methods(['GET', 'POST'])
def slider_banners_update(request):
    form_list = banners_form_list(request, SliderBannerForm)
    if request.method == 'POST':
        counter = 0
        for file in request.FILES.getlist('image'):
            form = SliderBannerForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                [obj.image, obj.url, obj.text] = [file, request.POST.getlist('url')[counter],
                                                  request.POST.getlist('text')[counter]]
                obj.save()
            counter += 1

        return redirect(reverse('home'))

    return render(request, 'admin_panel/banners/banners_sliders.html',
                  context={'form_list': form_list})


@require_http_methods(['GET', 'POST'])
def back_banners_update(request):
    form = BackBannerForm(request.POST or None, request.FILES or None, instance=None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect(reverse('home'))
    return render(request, 'admin_panel/banners/back_banner.html',
                  context={'form': form})


@require_http_methods(['GET', 'POST'])
def shares_banners_update(request):
    form_list = banners_form_list(request, SharesBannerForm)
    if request.method == 'POST':
        counter = 0
        for file in request.FILES.getlist('image'):
            form = SharesBannerForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                [obj.image, obj.url] = [file, request.POST.getlist('url')[counter]]
                obj.save()
            counter += 1

        return redirect(reverse('home'))

    return render(request, 'admin_panel/banners/shares_banners.html',
                  context={'form_list': form_list})

