from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

from register.forms.client import CreateClientForm, ClientForm


class UserRegisterView(CreateView):
    form_class = CreateClientForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


def login_page(request):
    context = {}
    return render(request, 'registration/login.html', context)


class UserEditView(UpdateView):
    form_class = ClientForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user
