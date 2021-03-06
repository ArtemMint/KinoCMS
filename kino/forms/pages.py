"""Pages forms"""

from django import forms

from kino.models.pages import HomePage, Contacts, Page


class HomepageForm(forms.ModelForm):
    """Home page form"""
    class Meta:
        """Meta class"""
        model = HomePage
        fields = "__all__"
        widgets = {
            'phone1': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': '+XX XXX XXX XX XX'}
            ),
            'phone2': forms.NumberInput(
                attrs={'class': 'form-control',
                       'placeholder': '+XX XXX XXX XX XX'}
            ),
            'seo_text': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Seo text...'}
            ),
            'seo_title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'SEO title of the cinema...'}
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


class ContactsForm(forms.ModelForm):
    """Contacts page form"""
    class Meta:
        """Meta class"""
        model = Contacts
        fields = "__all__"
        widgets = {
            'address': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Address...'}
            ),
            'coordinates': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Coordinates...'}
            ),
            'seo_title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'SEO title of the cinema...'}
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


class PageForm(forms.ModelForm):
    """Page form"""
    class Meta:
        """Meta class"""
        model = Page
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'Name...'}
            ),
            'description': forms.Textarea(
                attrs={'class': 'form-control',
                       'placeholder': 'Description...'}
            ),
            'seo_title': forms.TextInput(
                attrs={'class': 'form-control',
                       'placeholder': 'SEO title of the cinema...'}
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
