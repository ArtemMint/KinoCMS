from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from register.models import Client
from register.forms import CreateClientForm, EditProfileForm


class PasswordChangeView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name='registration/change_password.html'
    success_url = reverse_lazy('password_success')

class PasswordSuccessView(TemplateView):
    form_class = PasswordChangeForm
    template_name='registration/password_success.html'

class UserRegisterView(CreateView):
    form_class = CreateClientForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


def login_page(request):
    context={}
    return render(request,'registration/login.html', context)

class UserEditView(UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user