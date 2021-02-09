from django.views.generic import TemplateView, CreateView
from kino.models.banners import *
from kino.forms.banners import *


class AdminBannersView(CreateView):
    model = SliderBanner
    form_class = SliderBannerForm
    template_name = 'admin_panel/banners_sliders.html'
