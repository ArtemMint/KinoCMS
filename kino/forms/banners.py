"""This is the banners form module.

This module has baners forms for display view.
"""

__version__ = '0.1'
__author__ = 'Ivan Humeniuk'

from django import forms

from ..models.banners import *


class SliderBannerForm(forms.ModelForm):
    """SliderBannerForm has connect with model SliderBanner and fields:
    image, url,text."""
    class Meta:
        model = SliderBanner
        fields = '__all__'
        widgets = {
            'image': forms.FileInput(
                attrs={'class': 'form-control-file',
                       'accept': '.jpg, .jpeg, .png'}
            ),
            'url': forms.URLInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Input URL'}
            ),
            'text': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Input text'}
            )
        }


class BackBannerForm(forms.ModelForm):
    """BackBannerForm has connect with 
    model BackBanner and field: image."""
    class Meta:
        model = BackBanner
        fields = '__all__'
        widgets = {
            'image': forms.FileInput(
                attrs={'class': 'form-control-file',
                       'accept': '.jpg, .jpeg, .png'}
            ),
        }


class SharesBannerForm(forms.ModelForm):
    """SharesBannerForm has connect with
    model SharesBanner and fields:
    image, url."""
    class Meta:
        model = SharesBanner
        fields = '__all__'
        widgets = {
            'image': forms.FileInput(
                attrs={'class': 'form-control-file',
                       'accept': '.jpg, .jpeg, .png',
                       'style': "width:180px;"}
            ),
            'url': forms.URLInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Input URL'
                }
            ),
        }
