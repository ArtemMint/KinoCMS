from django.views.generic import ListView

from kino.models.shares import Shares


class SharesView(ListView):
    model = Shares
    template_name = 'kino/shares.html'