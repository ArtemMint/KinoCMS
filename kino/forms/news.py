from django import forms
from kino.models.news import News


class NewsForm(forms.ModelForm):
    preview = forms.ImageField()

    class Meta:
        model = News
        fields = ('name', 'description', 'status', 'preview', 'image1', 'image2', 'image3', 'image4', 'image5', 'video',
                  'seo_title', 'seo_keywords', 'seo_description')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of the News'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripton of the News'}),
            'status': forms.Select(),
            'preview': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Preview of the News'}),
            # 'image1': forms.FileInput(attrs={'class':'form-control'}),
            # 'image2': forms.FileInput(attrs={'class':'form-control'}),
            # 'image3': forms.FileInput(attrs={'class':'form-control'}),
            # 'image4': forms.FileInput(attrs={'class':'form-control'}),
            # 'image5': forms.FileInput(attrs={'class':'form-control'}),
            'video': forms.URLInput(),
            'seo_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SEO Title'}),
            'seo_keywords': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SEO Keywords'}),
            'seo_description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SEO Discriprions'}),
        }
