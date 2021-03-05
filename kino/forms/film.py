"""This is the film form module.

This module has film dorms for display view.
"""

__all__ = ['FilmForm', ]
__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django import forms

from kino.models.film import Film


class FilmForm(forms.ModelForm):
    """FilmForm has connect with Film model and fields:

    name, year, country, director, producer, music, scenarist,
    genre, description, video, premiere, seo_title, seo_keywords,
    seo_description."""
    two_dimensions = forms.BooleanField(
        label='2D',
        required=False,
        initial=False
    )
    three_dimensions = forms.BooleanField(
        label='3D',
        required=False,
        initial=False
    )
    imax = forms.BooleanField(
        label='IMAX',
        required=False,
        initial=False
    )

    class Meta:
        """Meta class"""
        model = Film
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Name of the film'
                       },
            ),
            'year': forms.Select(
                attrs={'class': 'form-control',
                       'placeholder': 'Year of the film'
                       }
            ),
            'country': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Country of the film'
                       }
            ),
            'director': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Director of the film'
                       }
            ),
            'producer': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Producer of the film'
                       }
            ),
            'music': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Music By'
                       }
            ),
            'scenarist': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Written By'
                       }
            ),
            'genre': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Genres'
                       }
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Description of the film',
                       'rows': '10'
                       }
            ),
            'video': forms.URLInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Video of the film'
                       }
            ),
            'premiere': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'type': 'date',
                },
            ),
            'preview': forms.FileInput(
                attrs={
                    'id': 'preview',
                    'class': 'form-control',
                }
            ),
            'duration': forms.TimeInput(
                format='%H:%M',
                attrs={
                       'placeholder': 'Example 1:50'}
            ),
            'seo_title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'SEO title of the cinema'
                       }
            ),
            'seo_keywords': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'SEO keywords of the cinema'
                       }
            ),
            'seo_description': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'SEO descripton of the cinema'
                       }
            ),
        }
        error_messages = {
            'duration': {
                'invalid': 'Try to input duration in format HH:MM',
            },
            'premiere': {
                'invalid': 'Try to input date in format MM/DD/YYYY',
            },
        }
