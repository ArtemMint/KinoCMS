from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.forms import inlineformset_factory
from kino.forms.shares import SharesForm
from kino.models.shares import Shares
from kino.models.image import SharesImage


class AdminSharesView(ListView):
    model = Shares
    template_name = 'admin_panel/shares/shares.html'
    ordering = ['-id']
    paginate_by = 15


def admin_shares_detail_view(request, shares_id):
    shares = Shares.objects.get(id=shares_id)
    image_list = SharesImage.objects.filter(shares=shares)

    template_name = 'admin_panel/shares/shares_detail.html'
    context = {'shares': shares, 'image_list': image_list}
    return render(request, template_name, context)


def admin_shares_create_view(request):
    SharesFormSet = inlineformset_factory(
        Shares, SharesImage, fields='__all__', extra=5, max_num=5)

    form = SharesForm()
    formset = SharesFormSet()

    if request.method == "POST":
        form = SharesForm(request.POST, request.FILES)
        formset = SharesFormSet(
            request.POST, request.FILES, instance=form.instance)
        if formset.is_valid() and form.is_valid():
            form.save()
            formset.save()
            return redirect('admin_shares')

    template_name = 'admin_panel/shares/shares_add.html'
    context = {'form': form, 'formset': formset}
    return render(request, template_name, context)


def admin_shares_update_view(request, shares_id):
    SharesFormSet = inlineformset_factory(
        Shares, SharesImage, fields='__all__', extra=5, max_num=5)
    shares = Shares.objects.get(id=shares_id)
    form = SharesForm(instance=shares)
    formset = SharesFormSet(instance=shares)

    if request.method == "POST":
        form = SharesForm(request.POST, request.FILES, instance=shares)
        formset = SharesFormSet(
            request.POST, request.FILES, instance=shares)
        if formset.is_valid() and form.is_valid():
            form.save()
            formset.save()
            return redirect('admin_shares')

    template_name = 'admin_panel/shares/shares_update.html'
    context = {'shares': shares, 'form': form, 'formset': formset}
    return render(request, template_name, context)


class AdminSharesDeleteView(DeleteView):
    model = Shares
    template_name = 'admin_panel/shares/shares_delete.html'
    success_url = reverse_lazy('admin_shares')
