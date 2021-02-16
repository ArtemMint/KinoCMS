from django import forms

from kino.models.news import News


class NewsForm(forms.ModelForm):
    preview = forms.ImageField()

    class Meta:
        model = News
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Name of the News'}
            ),
            'pub_date': forms.DateInput(
                attrs={'type': 'date'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Descripton of the News'}
            ),
            'status': forms.Select(),
            'preview': forms.FileInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Preview of the News'}
            ),
            'video': forms.URLInput(
                attrs={'class': 'form-control',
                       'placeholder': 'URL of the news'}
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
