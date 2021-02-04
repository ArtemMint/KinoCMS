from django.views.generic import TemplateView


class AdminStatisticsView(TemplateView):
    template_name = 'admin_panel/statistics.html'
