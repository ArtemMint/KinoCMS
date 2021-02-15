from django.shortcuts import render, redirect, reverse
from django.views.decorators.http import require_http_methods
from django.contrib.auth.models import User
from ...forms.mailing import MalingUsersForm, MalingGroupUsersForm
from ...repositories.users import get_all_users_email_list
from ...services.mailing import mail_users


@require_http_methods(['GET', 'POST'])
def mailing_all_users(request):
    """ This controller helps to send message from admin to all registered users."""
    form = MalingUsersForm(request.POST or None)
    if request.method == 'POST':
        mail_users(form, get_all_users_email_list())
        return redirect(reverse('home'))
    return render(request, 'admin_panel/mailing/mailing_all_users.html', context={'form': form})


@require_http_methods(['GET', 'POST'])
def mailing_group_of_users(request):
    """ This controller helps to send message from admin to a group of selected registered users """
    form = MalingGroupUsersForm(request.POST or None)
    if request.method == 'POST':
        mail_users(form, get_all_users_email_list(), group=True)
        return redirect(reverse('mailing_all_users'))
    return render(request, 'admin_panel/mailing/mailing_group_of_users.html',
                  context={'form': form})
