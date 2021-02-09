from django import forms
from kino.models.pages import HomePage, Contacts, Page


class HomepageForm(forms.ModelForm):

    class Meta:
        model = HomePage
        fields = "__all__"


class ContactsForm(forms.ModelForm):
    
    class Meta:
        model = Contacts
        fields = "__all__"


class PageForm(forms.ModelForm):
    
    class Meta:
        model = Page
        fields = "__all__"