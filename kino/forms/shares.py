from django import forms

from kino.models.shares import Shares


class SharesForm(forms.ModelForm):
    preview = forms.ImageField()

    class Meta:
        model = Shares
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Name of the Shares'}
            ),
            'pub_date': forms.DateInput(
                attrs={'class': 'form-control',
                       'type': 'date'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Descripton of the Shares'}
            ),
            'status': forms.Select(
                attrs={'class': 'form-control'}),
            'preview': forms.FileInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Preview of the Shares'}
            ),
            'video': forms.URLInput(
                attrs={'class': 'form-control',
                       'placeholder': 'URL of video'}
            ),
            'seo_title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'SEO Title'}
            ),
            'seo_keywords': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'SEO Keywords'}
            ),
            'seo_description': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'SEO Discriprions'}
            ),
        }
