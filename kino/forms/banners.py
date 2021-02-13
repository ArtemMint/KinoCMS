from ..models.banners import *
from django import forms


class SliderBannerForm(forms.ModelForm):
    class Meta:
        model = SliderBanner
        fields = '__all__'
        widgets = {
            'image': forms.FileInput(
                attrs={'accept': '.jpg, .jpeg, .png', 'style': "width:180px;"}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Url...'}),
            'text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Text...'})
        }


class BackBannerForm(forms.ModelForm):
    class Meta:
        model = BackBanner
        fields = '__all__'
        widgets = {'image': forms.FileInput(
            attrs={'accept': '.jpg, .jpeg, .png'})}


class SharesBannerForm(forms.ModelForm):
    class Meta:
        model = SharesBanner
        fields = '__all__'
        widgets = {
            'image': forms.FileInput(
                attrs={'accept': '.jpg, .jpeg, .png', 'style': "width:180px;"}),
            'url': forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Url...'}),
        }
