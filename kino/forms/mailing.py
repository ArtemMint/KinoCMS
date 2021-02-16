from django import forms

from kino.repositories.users import get_all_users_email_list


class MalingUsersForm(forms.Form):
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
    OPTIONS = [(f'{email}', f'{email}')
               for email in get_all_users_email_list()]

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
