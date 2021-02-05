from django.views.generic import TemplateView


class AdminBannersView(TemplateView):
    template_name = 'admin_panel/banners_sliders.html'
