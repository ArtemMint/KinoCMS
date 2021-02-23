from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from register.forms.client import *


def user_register_view(request):
    form = RegisterUserForm

    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            form.save()
            return redirect('login')

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )


def user_login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('edit_profile')

    return render(
        request,
        'registration/login.html',
        {}
    )


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

    return render(
        request,
        'registration/edit_profile.html',
        {'client_form': client_form, 'user_form': user_form}
    )
