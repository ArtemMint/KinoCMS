from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from kino.models import Film, Cinema


class FilmForm(forms.ModelForm):
    preview = forms.ImageField()
    class Meta:
        model = Film
        fields = ('name', 'year', 'country', 'director', 'producer', 'music', 'scenarist', 'genre', 'description', 'preview')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of the film'}),
            'year': forms.Select(attrs={'class':'form-control'}),
            'country': forms.TextInput(attrs={'class':'form-control'}),
            'director': forms.TextInput(attrs={'class':'form-control'}),
            'producer': forms.TextInput(attrs={'class':'form-control'}),
            'music': forms.TextInput(attrs={'class':'form-control'}),
            'scenarist': forms.TextInput(attrs={'class':'form-control'}),
            'genre': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'preview': forms.FileInput(attrs={'class':'form-control'}),
        }

class CinemaForm(forms.ModelForm):
    preview = forms.ImageField()
    class Meta:
        model = Cinema
        fields = ('name', 'description', 'preview')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of the Cinema'}),
            'description': forms.Textarea(attrs={'class':'form-control'}),
            'preview': forms.FileInput(attrs={'class':'form-control'}),
        }





# REGISTER FORMS
class SignInForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of the Cinema'}),
            'password': forms.TextInput(attrs={'class':'form-control'}),
        }


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)