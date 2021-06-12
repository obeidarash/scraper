from django import forms
from django.core import validators


class ScrapeForm(forms.Form):
    url = forms.URLField(
        widget=forms.URLInput(
            attrs={'placeholder': '', 'class': 'form-control'}),
        label='Link',
        validators=[
            validators.URLValidator(message='{url} not a url'),
        ]
    )
