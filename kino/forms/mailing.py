from django import forms


class MalingUsersForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject...'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your message...'}))

    widgets = {
        'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject...'}),
        'message': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your message...'})
    }

