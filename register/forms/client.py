from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from register.models.client import Client
from utils import current_year


class UserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example username: example1551'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Example email: example@gmail.com'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }


class ClientForm(UserChangeForm):

    class Meta:
        # years_to_display = range(current_year() - 100, current_year())
        model = Client
        fields = '__all__'
        exclude = ('user',)
        widgets = {
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: Green street, 15'}),
            'num_card': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: 1234 2345 4567 5678'}),
            'language': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: +380971234567'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: Kyiv'}),
        }


class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1',
                  'password2',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input username: example1551'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Input email: example@gmail.com'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Input password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeate password'}),
        }


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1',
                  'password2', 'first_name', 'last_name',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Input username: example1551'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Input email: example@gmail.com'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Input password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Repeate password'}),
        }


class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        exclude = ('user', )
        widgets = {
            'birth_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: Green street, 15'}),
            'num_card': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: 1234 2345 4567 5678'}),
            'language': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: +380971234567'}),
            'city': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: Kyiv'}),
        }
