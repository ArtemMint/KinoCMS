from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from register.models.client import Client
from utils import current_year


class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')


class ClientForm(UserChangeForm):
    class Meta:
        years_to_display = range(current_year() - 100, current_year())
        model = Client
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'birth_date': forms.SelectDateWidget(years=years_to_display),
            'gender': forms.Select(),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class CreateClientForm(UserCreationForm):
    class Meta:
        model = Client
        fields = '__all__'
