from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from register.models.client import Client
from register.forms.client import ClientForm, UserForm, CreateClientForm, CreateUserForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import Http404


def adminUserListView(request):
    contact_list = User.objects.order_by('-id')
    paginator = Paginator(contact_list, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'page_obj': page_obj}
    return render(request, 'admin_panel/users/users.html', context)


def adminUserCreateView(request):

    user_form = CreateUserForm()
    client_form = CreateClientForm()

    if request.method == "POST" :
        user_form = CreateUserForm(request.POST)
        client_form = CreateClientForm(request.POST)
        if user_form.is_valid() and client_form.is_valid():
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user_form.save()
            client_form.save()
            return redirect('admin_users')

    context = {'user_form': user_form, 'client_form': client_form}
    return render(request, 'admin_panel/users/user_add.html', context)


def adminUserUpdateView(request, user_id):

    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        client_form = ClientForm(
            request.POST, request.FILES, instance=user.client)

        if client_form.is_valid() and user_form.is_valid():
            user_form.save()
            client_form.save()
            return redirect('admin_users')
    else:
        user_form = UserForm(instance=user)
        client_form = ClientForm(instance=user.client)

    context = {'client_form': client_form, 'user_form': user_form}
    return render(request, 'admin_panel/users/user_update.html', context)


def adminUserDeleteView(request, user_id):
    """
    Delete Hall in the Cinema
    """
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.delete()
        return redirect('admin_users')
    context = {'user': user}
    return render(
        request,
        'admin_panel/users/user_delete.html', context
    )