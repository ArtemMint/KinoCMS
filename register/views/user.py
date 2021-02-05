from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404

from django.contrib.auth.models import User
from register.models.client import Client

from register.forms.client import CreateClientForm, ClientForm
from register.forms.client import ClientForm, UserForm


class UserRegisterView(CreateView):
    form_class = CreateClientForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


def login_page(request):
    context = {}
    return render(request, 'registration/login.html', context)


def userUpdateView(request):
    try:
        user = request.user
        client = Client.objects.get(user=user)
    except client.DoesNotExist:
        raise Http404("Client does not exist")
    if request.method == 'POST':
        client_form = ClientForm(
            request.POST, request.FILES, instance=request.user.client)
        user_form = UserForm(request.POST, instance=request.user)
        if client_form.is_valid() and user_form.is_valid():
            user_form.save()
            client_form.save()
            return redirect('home')
    else:
        client_form = ClientForm(instance=request.user.client)
        user_form = UserForm(instance=request.user)

    context = {'client_form': client_form, 'user_form': user_form}
    return render(request, 'registration/edit_profile.html', context)
