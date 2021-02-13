from django import forms
from kino.models.film import Film


class FilmForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = '__all__'
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
            'premiere': forms.DateInput(attrs={'type': 'date'}),
            'seo_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SEO title of the cinema'}),
            'seo_keywords': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SEO keywords of the cinema'}),
            'seo_description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'SEO descripton of the cinema'}),
        }
