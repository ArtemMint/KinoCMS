from django.views.generic import TemplateView


class AdminBannersSlidersView(TemplateView):
    template_name = 'admin_panel/banners_sliders.html'
