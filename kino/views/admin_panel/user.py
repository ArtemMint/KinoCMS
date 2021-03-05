from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator

from register.forms.client import ClientForm, UserForm, CreateUserForm


@permission_required('is_staff')
def adminUserListView(request):
    contact_list = User.objects.order_by('-id')
    paginator = Paginator(contact_list, 15)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'admin_panel/users/users.html',
        {
            'page_obj': page_obj,
        }
    )


@permission_required('is_staff')
def adminUserCreateView(request):

    user_form = CreateUserForm()
    # client_form = CreateClientForm()

    if request.method == "POST":
        user_form = CreateUserForm(request.POST)
        # client_form = CreateClientForm(request.POST)
        if user_form.is_valid():
            # if user_form.is_valid() and client_form.is_valid():
            user_form.save(commit=False)
            # client_form.save(commit=False)
            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password1')
            user_form.save()
            # client_form.user = username
            # client_form.save()
            return redirect('admin_users')

    return render(
        request,
        'admin_panel/users/user_add.html',
        {
            'user_form': user_form,
        }
    )


@permission_required('is_staff')
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

    return render(
        request,
        'admin_panel/users/user_update.html',
        {
            'client_form': client_form,
            'user_form': user_form,
        }
    )


@permission_required('is_staff')
def adminUserDeleteView(request, user_id):
    """
    Delete Hall in the Cinema
    """
    user = get_object_or_404(User, id=user_id)

    if request.method == "POST":
        user.delete()
        return redirect('admin_users')

    return render(
        request,
        'admin_panel/users/user_delete.html',
        {
            'user': user,
        }
    )
