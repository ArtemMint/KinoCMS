from django.views.generic import TemplateView


class AdminPagesView(TemplateView):
    template_name = 'admin_panel/pages.html'
