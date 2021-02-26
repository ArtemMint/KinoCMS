from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class PasswordChangeView_(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name='registration/change_password.html'
    success_url = reverse_lazy('password_success')


class PasswordSuccessView(TemplateView):
    form_class = PasswordChangeForm
    template_name='registration/password_success.html'