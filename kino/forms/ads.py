"""This is the ads form module.

This module has ads image and url view.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django import forms

from ..models.ads import ADS


class ADSForm(forms.ModelForm):
    """ADSForm has connect with model ADS and fields:
    image, url."""
    class Meta:
        """Meta class"""
        model = ADS
        fields = '__all__'
        widgets = {
            'image': forms.FileInput(
                attrs={'class': 'form-control-file',
                       'accept': '.jpg, .jpeg, .png, .gif'}
            ),
            'url': forms.URLInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Input URL'}
            ),
        }
