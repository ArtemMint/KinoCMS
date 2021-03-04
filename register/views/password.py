"""This is the password module.

This module has password change views.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class PasswordChangeView_(PasswordChangeView):
    """Password change view

    Args:
        PasswordChangeView ([type]): [description]
    """
    form_class = PasswordChangeForm
    template_name='registration/change_password.html'
    success_url = reverse_lazy('password_success')


class PasswordSuccessView(TemplateView):
    """Password success view after password change

    Args:
        TemplateView ([type]): [description]
    """
    form_class = PasswordChangeForm
    template_name='registration/password_success.html'