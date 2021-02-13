from django import forms
from kino.models.cinema import Cinema, CinemaHall


class CinemaForm(forms.ModelForm):
    preview = forms.ImageField()
    class Meta:
        model = Cinema
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of the cinema'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripton of the cinema'}),
            'preview': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Preview of the cinema'}),
            'conditions': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Condition of the cinema'}),
            'seo_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SEO title of the cinema'}),
            'seo_keywords': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SEO keywords of the cinema'}),
            'seo_description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'SEO descripton of the cinema'}),
        }


class CinemaHallForm(forms.ModelForm):
    scheme = forms.ImageField(widget=forms.FileInput)
    preview = forms.ImageField(widget=forms.FileInput)
    class Meta:
        model = CinemaHall
        fields = '__all__'
        exclude = ('cinema','created_date',)
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of the cinemahall'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripton of the cinemahall'}),
            'preview': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Preview of the cinemahall'}),
            'seo_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SEO title of the cinema'}),
            'seo_keywords': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SEO keywords of the cinema'}),
            'seo_description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'SEO descripton of the cinema'}),
        }