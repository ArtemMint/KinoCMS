from django import forms
from kino.models.film import Film


class FilmForm(forms.ModelForm):
    preview = forms.ImageField()
    image1 = forms.ImageField()
    image2 = forms.ImageField()
    image3 = forms.ImageField()
    image4 = forms.ImageField()
    image5 = forms.ImageField()

    class Meta:
        model = Film
        fields = (
            'name', 'year', 'country', 'director', 'producer', 'music', 'scenarist', 'genre', 'description', 'preview',
            'video', 'image1', 'image2', 'image3', 'image4', 'image5')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the film'}),
            'year': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Year of the film'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country of the film'}),
            'director': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Director of the film'}),
            'producer': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Producer of the film'}),
            'music': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Music By'}),
            'scenarist': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Written By'}),
            'genre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Genre of the film'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description of the film'}),
            'video': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Video of the film'}),
            'preview': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image of the film'}),
            'image1': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image of the film'}),
            'image2': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image of the film'}),
            'image3': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image of the film'}),
            'image4': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image of the film'}),
            'image5': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Image of the film'}),
        }
