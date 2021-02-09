from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from kino.forms.shares import SharesForm
from kino.models.shares import Shares


class AdminSharesView(ListView):
    model = Shares
    template_name = 'admin_panel/shares/shares.html'
    ordering = ['-id']


class AdminSharesDetailView(DetailView):
    model = Shares
    template_name = 'admin_panel/shares/shares_detail.html'


class AdminSharesAddView(CreateView):
    model = Shares
    form_class = SharesForm
    template_name = 'admin_panel/shares/shares_add.html'


class AdminSharesUpdateView(UpdateView):
    model = Shares
    form_class = SharesForm
    template_name = 'admin_panel/shares/shares_update.html'


class AdminSharesDeleteView(DeleteView):
    model = Shares
    template_name = 'admin_panel/shares/shares_delete.html'
    success_url = reverse_lazy('admin_shares')