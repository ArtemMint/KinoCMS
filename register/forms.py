from django import forms
from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from register.models import Client


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'})),
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'})),
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'})),
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'})),


    class Meta:
        model = Client
        fields = ('city',)

class ClientForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username',)