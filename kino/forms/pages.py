from django import forms
from kino.models.pages import HomePage, Contacts, Page


class HomepageForm(forms.ModelForm):
    class Meta:
        model = HomePage
        fields = "__all__"
        widgets = {
            'phone1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '+XX XXX XXX XX XX'}),
            'phone2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '+XX XXX XXX XX XX'}),
            'seo_text': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seo text..'}),
            'seo_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'SEO title of the cinema...'}),
            'seo_keywords': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'SEO keywords of the cinema'}),
            'seo_description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'SEO descripton of the cinema'}),
        }

class ContactsForm(forms.ModelForm):

    class Meta:
        model = Contacts
        fields = "__all__"


class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = "__all__"
