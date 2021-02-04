from django import forms
from kino.models.shares import Shares


class SharesForm(forms.ModelForm):
    preview = forms.ImageField()

    class Meta:
        model = Shares
        fields = ('name', 'description','status', 'preview', 'image1', 'image2', 'image3', 'image4', 'image5', 'video', 'seo_title', 'seo_keywords', 'seo_description')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name of the Shares'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Descripton of the Shares'}),
            'status': forms.Select(),
            'preview': forms.FileInput(attrs={'class':'form-control', 'placeholder':'Preview of the Shares'}),
            # 'image1': forms.FileInput(attrs={'class':'form-control'}),
            # 'image2': forms.FileInput(attrs={'class':'form-control'}),
            # 'image3': forms.FileInput(attrs={'class':'form-control'}),
            # 'image4': forms.FileInput(attrs={'class':'form-control'}),
            # 'image5': forms.FileInput(attrs={'class':'form-control'}),
            'video' : forms.URLInput(),
            'seo_title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SEO Title'}),
            'seo_keywords': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SEO Keywords'}),
            'seo_description': forms.TextInput(attrs={'class':'form-control', 'placeholder':'SEO Discriprions'}),
        }