"""Mailing module"""

__version__ = '0.1'
__author__ = 'Ivan Humeniuk'

from django import forms

# from kino.repositories.users import get_all_users_email_list


class MalingUsersForm(forms.Form):
    """MalingUsersForm"""
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Subject...'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control',
               'placeholder': 'Your message...'}))

    widgets = {
        'subject': forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Subject...'}
        ),
        'message': forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Your message...'}
        )
    }


class MalingGroupUsersForm(forms.Form):
    """MalingGroupUsersForm"""
    # OPTIONS = [(f'{email}', f'{email}')
    #            for email in get_all_users_email_list()]
    OPTIONS = [(1,1),(2,2),]

    emails = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=OPTIONS
    )
    subject = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Subject...'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control',
               'placeholder': 'Your message...'}))

    widgets = {
        'subject': forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Subject...'}
        ),
        'message': forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Your message...'}
        )
    }
