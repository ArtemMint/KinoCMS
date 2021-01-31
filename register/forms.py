import datetime
from django import forms
from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from register.models import Client


class EditProfileForm(UserChangeForm):

    class Meta:

        years_to_display = range(datetime.datetime.now().year - 100, datetime.datetime.now().year)
        model = Client
        fields = ('address','phone','city','birth_date','gender',)
        widgets = {
            'birth_date':forms.SelectDateWidget(years=years_to_display),
            'gender':forms.Select(),
        }


class ClientForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username',)