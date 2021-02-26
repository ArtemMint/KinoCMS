from django.forms import modelformset_factory
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render, reverse
from django.contrib.auth.decorators import permission_required

from kino.models.banners import *
from kino.forms.banners import *
from kino.services.banners import *


@permission_required('is_staff')
@require_http_methods(['GET', 'POST'])
def slider_banners_update(request):
    SliderFormSet = modelformset_factory(
        SliderBanner,
        SliderBannerForm,
        fields=(
            'image',
            'url',
            'text',
        ),
        extra=5,
        max_num=5,
        can_delete=True
    )

    formset = SliderFormSet()

    if request.method == "POST":
        formset = SliderFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect('admin_statistics')

    return render(
        request,
        'admin_panel/banners/slider_banners.html',
        {'formset': formset}
    )


@permission_required('is_staff')
@require_http_methods(['GET', 'POST'])
def back_banners_update(request):
    form = BackBannerForm(
        request.POST,
        request.FILES,
        instance=get_background()
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('admin_statistics')

    return render(
        request,
        'admin_panel/banners/back_banner.html',
        {'form': form}
    )


@permission_required('is_staff')
@require_http_methods(['GET', 'POST'])
def shares_banners_update(request):
    SharesFormSet = modelformset_factory(
        SharesBanner,
        SharesBannerForm,
        fields=(
            'image',
            'url',
        ),
        extra=5,
        max_num=5,
        can_delete=True
    )

    formset = SharesFormSet()

    if request.method == "POST":
        formset = SharesFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect('admin_statistics')

    return render(
        request,
        'admin_panel/banners/shares_banners.html',
        {'formset': formset}
    )
