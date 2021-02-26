from django.shortcuts import render, redirect
from django.forms import modelformset_factory
from django.contrib.auth.decorators import permission_required

from kino.forms.ads import ADSForm
from kino.repositories.ads import *


@permission_required('is_staff')
def admin_ads_view(request):
    ADSFormSet = modelformset_factory(ADS, ADSForm, fields=('image','url'), extra=2, max_num=2,)
    formset = ADSFormSet()
    
    if request.method == "POST":
        formset = ADSFormSet(request.POST, request.FILES)
        if formset.is_valid():
            formset.save()
            return redirect('admin_statistics')
    
    return render(
        request,
        'admin_panel/ads.html',
        {'ads': get_ads_list, 'formset': formset}
    )