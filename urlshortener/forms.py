from django import forms
from django.forms import fields
from .models import ShortedLink

class LinkShortForm(forms.ModelForm):
    original_link = forms.CharField(max_length=200)
    class Meta:
        model = ShortedLink
        fields = [
            'original_link'
        ]