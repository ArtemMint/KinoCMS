from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from register.models.client import Client
from register.forms.client import *


def user_register_view(request):
    form = RegisterUserForm

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            form.save()
            return redirect('login')

    template_name = 'registration/register.html'
    context = {'form': form}
    return render(request, template_name, context)


def user_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('edit_profile')

    context = {}
    return render(request, 'registration/login.html', context)


def user_update_view(request):
    user = request.user
    client = Client.objects.get(user=user)
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
