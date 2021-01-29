from django import forms
from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from kino.models import Film, Cinema, News


class FilmForm(forms.ModelForm):
    preview = forms.ImageField()
    image1 = forms.ImageField()
    image2 = forms.ImageField()
    image3 = forms.ImageField()
    image4 = forms.ImageField()
    image5 = forms.ImageField()
    
    class Meta:
        model = Film
        fields = ('name', 'year', 'country', 'director', 'producer', 'music', 'scenarist', 'genre', 'description', 'preview', 'image1', 'image2', 'image3', 'image4', 'image5')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of the film'}),
            'year': forms.Select(attrs={'class':'form-control', 'placeholder':'Year of the film'}),
            'country': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Country of the film'}),
            'director': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Director of the film'}),
            'producer': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Producer of the film'}),
            'music': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Music By'}),
            'scenarist': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Written By'}),
            'genre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Genre of the film'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Description of the film'}),
            'preview': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Image of the film'}),
            'image1': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Image of the film'}),
            'image2': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Image of the film'}),
            'image3': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Image of the film'}),
            'image4': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Image of the film'}),
            'image5': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Image of the film'}),
        }

class CinemaForm(forms.ModelForm):
    preview = forms.ImageField()
    class Meta:
        model = Cinema
        fields = ('name', 'description', 'preview', 'image1', 'image2', 'image3', 'image4', 'image5')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of the cinema'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripton of the cinema'}),
            'preview': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Preview of the cinema'}),
            'image1': forms.FileInput(attrs={'class':'form-control'}),
            'image2': forms.FileInput(attrs={'class':'form-control'}),
            'image3': forms.FileInput(attrs={'class':'form-control'}),
            'image4': forms.FileInput(attrs={'class':'form-control'}),
            'image5': forms.FileInput(attrs={'class':'form-control'}),
        }


class NewsForm(forms.ModelForm):
    preview = forms.ImageField()
    image1 = forms.ImageField()
    image2 = forms.ImageField()
    image3 = forms.ImageField()
    image4 = forms.ImageField()
    image5 = forms.ImageField()

    class Meta:
        model = News
        fields = ('name', 'description','status', 'preview', 'image1', 'image2', 'image3', 'image4', 'image5', 'video', 'seo_title', 'seo_keywords', 'seo_description')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of the News'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripton of the News'}),
            'status': forms.CheckboxInput(),
            'preview': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Preview of the News'}),
            'image1': forms.FileInput(attrs={'class':'form-control'}),
            'image2': forms.FileInput(attrs={'class':'form-control'}),
            'image3': forms.FileInput(attrs={'class':'form-control'}),
            'image4': forms.FileInput(attrs={'class':'form-control'}),
            'image5': forms.FileInput(attrs={'class':'form-control'}),
            'video' : forms.URLInput(),
            'seo_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SEO Title'}),
            'seo_keywords': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SEO Keywords'}),
            'seo_description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SEO Discriprions'}),
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