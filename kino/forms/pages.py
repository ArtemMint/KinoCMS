from django import forms
from kino.models.pages import HomePage


class HomepageForm(forms.ModelForm):

    class Meta:
        model = HomePage
        fields = "__all__"