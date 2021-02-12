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
        }


class CinemaHallForm(forms.ModelForm):
    preview = forms.ImageField()
    class Meta:
        model = CinemaHall
        fields = '__all__'
        exclude = ('cinema','created_date',)
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of the cinemahall'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripton of the cinemahall'}),
            'preview': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Preview of the cinemahall'}),
        }