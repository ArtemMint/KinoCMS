from django import forms


class MalingForm(forms.Form):
    subject = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Text...'})
    message = forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your message...'})
