from django import forms
from .models import ImageTableSettings


class ImageTableSettingsForm(forms.ModelForm):
    class Meta:
        model = ImageTableSettings
        exclude = []
