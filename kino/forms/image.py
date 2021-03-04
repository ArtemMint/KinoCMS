"""This is the image form module.

This module has image dorms for display view.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django import forms

from kino.models.image import *

GENRES = (
    ('Sci-Fi', 'Sci-Fi'),
    ('Detective', 'Detective'),
    ('Horror', 'Horror'),
    ('Anime', 'Anime'),
    ('Thriller', 'Thriller'),
)


class FilmImageForm(forms.ModelForm):
    """FilmImageForm has connect with FilmImage model and fields:
    """
    class Meta:
        """Meta class"""
        model = FilmImage
        fields = '__all__'
        widgets = {
            'image': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'onchange': 'preview_image(event)',
                }
            ),
        }
