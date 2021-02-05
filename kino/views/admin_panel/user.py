from django.views.generic import ListView, UpdateView, DeleteView
from django.contrib.auth.models import User
from register.models.client import Client
from register.forms.client import ClientForm, UserForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import Http404


# class AdminUsersView(ListView):
#     paginate_by = 5
#     model = Client
#     template_name = 'admin_panel/users/users.html'
#     ordering = ['-id']


# class AdminUsersUpdateView(UpdateView):
#     model = Client
#     form_class = EditProfileForm
#     template_name = 'admin_panel/users/user_update.html'

#     def get_success_url(self):
#         return reverse('admin_users')

def adminUserListView(request):
    contact_list = User.objects.all()
    paginator = Paginator(contact_list, 5)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'admin_panel/users/users.html', {'page_obj': page_obj})


def adminUserUpdateView(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        client = Client.objects.get(user=user)
        # client = request.user.client
    except client.DoesNotExist:
        raise Http404("Client does not exist")
    if request.method == 'POST':
        client_form = ClientForm(
            request.POST, request.FILES, instance=user.client)
        user_form = UserForm(request.POST, instance=user)
        if client_form.is_valid() and user_form.is_valid():
            user_form.save()
            client_form.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('admin_users')
    else:
        client_form = ClientForm(instance=user.client)
        user_form = UserForm(instance=user)

    context = {'client_form': client_form, 'user_form': user_form}
    return render(request, 'admin_panel/users/user_update.html', context)


class AdminUserDeleteView(DeleteView):
    model = Client
    template_name = 'admin_panel/users/user_delete.html'
    success_url = reverse_lazy('admin_users')

    def get_success_url(self):
        return reverse('admin_users')
