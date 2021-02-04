from django.views.generic import TemplateView


class AdminMailingView(TemplateView):
    template_name = 'admin_panel/mailing.html'
