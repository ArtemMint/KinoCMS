"""This is the cinema form module.

This module has cinema and cinema hall forms for display view.
"""

__all__ = ['CinemaForm', 'CinemaHallForm', ]
__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django import forms

from kino.models.cinema import Cinema, CinemaHall


class CinemaForm(forms.ModelForm):
    """ CinemaForm has connect with model Cinema and fields:
    name, descriptions, preview, conditions,
    seo_title, seo_keywords, seo_descriptions."""
    preview = forms.ImageField()

    class Meta:
        """Meta class"""
        model = Cinema
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Name of the cinema'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Descripton of the cinema'}
            ),
            'preview': forms.FileInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Preview of the cinema'}
            ),
            'conditions': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Condition of the cinema'}
            ),
            'seo_title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'SEO title of the cinema'}
            ),
            'seo_keywords': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'SEO keywords of the cinema'}
            ),
            'seo_description': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'SEO descripton of the cinema'}
            ),
        }


class CinemaHallForm(forms.ModelForm):
    """CinemaHallForm has connect with model CinemaHall and fields:
    cinema, name, scheme, create_date,descriptions,
    preview, seo_title, seo_keywords, seo_descriptions.
    """
    scheme = forms.ImageField()
    preview = forms.ImageField()

    class Meta:
        """Meta class"""
        model = CinemaHall
        fields = '__all__'
        exclude = (
            'cinema',
            'created_date',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Name of the cinemahall'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Descripton of the cinemahall'}
            ),
            'preview': forms.FileInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Preview of the cinemahall'}
            ),
            'seo_title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'SEO title of the cinema'}
            ),
            'seo_keywords': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'SEO keywords of the cinema'}
            ),
            'seo_description': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'SEO descripton of the cinema'}
            ),
        }
