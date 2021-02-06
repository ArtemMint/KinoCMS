from django import forms
from kino.models.cinema import Cinema


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