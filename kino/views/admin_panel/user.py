from django.views.generic import ListView, UpdateView, DeleteView
from register.models import Client
from register.forms import EditProfileForm
from django.urls import reverse_lazy, reverse


class AdminUsersView(ListView):
    model = Client
    template_name = 'admin_panel/users/users.html'
    ordering = ['-id']


class AdminUsersUpdateView(UpdateView):
    model = Client
    form_class = EditProfileForm
    template_name = 'admin_panel/users/user_update.html'

    def get_success_url(self):
        return reverse('admin_users')


class AdminUserDeleteView(DeleteView):
    model = Client
    template_name = 'admin_panel/users/user_delete.html'
    success_url = reverse_lazy('admin_users')

    def get_success_url(self):
        return reverse('admin_users')
