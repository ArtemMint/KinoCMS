from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import permission_required

from kino.forms.shares import SharesForm
from kino.models.shares import Shares
from kino.models.image import SharesImage
from ...repositories.shares import *


class AdminSharesView(ListView):
    model = Shares
    template_name = 'admin_panel/shares/shares.html'
    ordering = ['-id']
    paginate_by = 15


@permission_required('is_staff')
def admin_shares_detail_view(request, shares_id):

    return render(
        request,
        'admin_panel/shares/shares_detail.html',
        {
            'shares': get_shares_by_id(shares_id),
            'image_list': get_shares_gallery(get_shares_by_id(shares_id))
        },
    )


@permission_required('is_staff')
def admin_shares_create_view(request):
    SharesFormSet = inlineformset_factory(
        Shares,
        SharesImage,
        fields='__all__',
        extra=5,
        max_num=5,
    )

    form = SharesForm()
    formset = SharesFormSet()

    if request.method == "POST":
        form = SharesForm(request.POST, request.FILES)
        formset = SharesFormSet(
            request.POST,
            request.FILES,
            instance=form.instance
        )
        if formset.is_valid() and form.is_valid():
            form.save()
            formset.save()
            return redirect('admin_shares')

    return render(
        request,
        'admin_panel/shares/shares_add.html',
        {
            'form': form,
            'formset': formset,
        }
    )


@permission_required('is_staff')
def admin_shares_update_view(request, shares_id):
    SharesFormSet = inlineformset_factory(
        Shares,
        SharesImage,
        fields='__all__',
        extra=5,
        max_num=5,
    )
    
    form = SharesForm(instance=get_shares_by_id(shares_id))
    formset = SharesFormSet(instance=get_shares_by_id(shares_id))

    if request.method == "POST":
        form = SharesForm(
            request.POST,
            request.FILES,
            instance=get_shares_by_id(shares_id),
        )
        formset = SharesFormSet(
            request.POST,
            request.FILES,
            instance=get_shares_by_id(shares_id),
        )
        if formset.is_valid() and form.is_valid():
            form.save()
            formset.save()
            return redirect('admin_shares')

    return render(
        request,
        'admin_panel/shares/shares_update.html',
        {
            'shares': get_shares_by_id(shares_id),
            'form': form,
            'formset': formset,
        }
    )


class AdminSharesDeleteView(DeleteView):
    model = Shares
    template_name = 'admin_panel/shares/shares_delete.html'
    success_url = reverse_lazy('admin_shares')
