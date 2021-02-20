"""This is the schedule form module.

This module has schedule dorms for display view.
"""

__version__ = '0.1'
__author__ = 'Artem Yurchak'

from django import forms

from kino.models.schedule import Schedule


class ScheduleForm(forms.ModelForm):
    """ScheduleForm has connect with Film model and fields:

    film, cinemahall, date, time."""
    class Meta:
        model = Schedule
        fields = '__all__'
        widgets = {
            'film': forms.Select(
                attrs={'class': 'form-control',
                       'placeholder': 'Choose film..'}
            ),
            'cinemahall': forms.Select(
                attrs={'class': 'form-control',
                       'placeholder': 'Choose cinema hall..'}
            ),
            'cost': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Minimun cost of the ticket..'}
            ),
            'date': forms.DateTimeInput(
                attrs={'class': 'form-control',
                       'type': 'date',
                       'placeholder': 'Input date of session..'}
            ),
            'time': forms.TimeInput(
                format='%H:%M',
                attrs={'class': 'form-control',
                       'type': 'time',
                       'placeholder': 'Input duration of film..'}
            ),
        }
