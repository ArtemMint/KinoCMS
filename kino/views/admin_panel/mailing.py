from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from ...forms.mailing import MalingForm
from ...repositories.users import get_all_users_email_list
from ...services.mailing import mail_users


class AdminMailingView(TemplateView):
    template_name = 'admin_panel/mailing.html'


@require_http_methods(['GET', 'POST'])
def mailing_list_form(request):
    """ This controller helps to send message from admin to a couple select users,
        that are registered"""
    form = MalingForm(request.POST or None)
    if request.method == 'POST':
        users_list = None
        pass
    return render(request, 'admin_panel/mailing/mailing_form_list.html', context={'form': form})


@require_http_methods(['POST'])
def mailing_all_users(request):
    """ This controller helps to send message from admin to all users,
    that are registered"""
    mail_users(request, get_all_users_email_list())
    return redirect(reverse('home'))
