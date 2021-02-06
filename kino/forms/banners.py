from ..models.banners import *
from django import forms


class SliderBannerForm(forms.ModelForm):
    class Meta:
        model = SliderBanner
        fields = '__all__'
        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Url...'}),
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Text'})
        }
