from django import forms
from django.forms.widgets import CheckboxInput
from django.forms.utils import flatatt
from django.utils.html import format_html
from django.utils.encoding import force_text

from .models import ImageTableSettings, VideoTableSettings, AudioTableSettings


class PropellerBooleanWidget(CheckboxInput):
    def render(self, name, value, attrs=None):
        extra_style = {'class': 'checkbox pmd-checkbox pmd-checkbox-ripple-effect'}
        if attrs:
            attrs.update(extra_style)
        else:
            attrs = extra_style
        final_attrs = self.build_attrs(attrs, type='checkbox', name=name)
        if self.check_test(value):
            final_attrs['checked'] = 'checked'
        if not (value is True or value is False or value is None or value == ''):
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(value)
        print(final_attrs)
        res = format_html('<input{} />', flatatt(final_attrs))
        print(res)
        return res


class BooleanField(forms.BooleanField):
    widget = PropellerBooleanWidget


class ImageTableSettingsForm(forms.ModelForm):
    image_show_preview = forms.BooleanField(required=False)
    image_show_description = forms.BooleanField(required=False)
    image_show_type = forms.BooleanField(required=False)
    image_show_size = forms.BooleanField(required=False)
    image_show_path = forms.BooleanField(required=False)
    image_show_filesize = forms.BooleanField(required=False)
    image_show_modified = forms.BooleanField(required=False)
    image_show_created = forms.BooleanField(required=False)
    image_show_rating = forms.BooleanField(required=False)
    image_show_tags = forms.BooleanField(required=False)
    image_show_relations = forms.BooleanField(required=False)

    class Meta:
        model = ImageTableSettings
        exclude = []


class VideoTableSettingsForm(forms.ModelForm):
    video_show_preview = forms.BooleanField(required=False)
    video_show_description = forms.BooleanField(required=False)
    video_show_type = forms.BooleanField(required=False)
    video_show_length = forms.BooleanField(required=False)
    video_show_path = forms.BooleanField(required=False)
    video_show_filesize = forms.BooleanField(required=False)
    video_show_modified = forms.BooleanField(required=False)
    video_show_created = forms.BooleanField(required=False)
    video_show_rating = forms.BooleanField(required=False)
    video_show_tags = forms.BooleanField(required=False)
    video_show_relations = forms.BooleanField(required=False)

    class Meta:
        model = VideoTableSettings
        exclude = []


class AudioTableSettingsForm(forms.ModelForm):
    audio_show_preview = forms.BooleanField(required=False)
    audio_show_description = forms.BooleanField(required=False)
    audio_show_type = forms.BooleanField(required=False)
    audio_show_length = forms.BooleanField(required=False)
    audio_show_path = forms.BooleanField(required=False)
    audio_show_filesize = forms.BooleanField(required=False)
    audio_show_modified = forms.BooleanField(required=False)
    audio_show_created = forms.BooleanField(required=False)
    audio_show_rating = forms.BooleanField(required=False)
    audio_show_tags = forms.BooleanField(required=False)
    audio_show_relations = forms.BooleanField(required=False)

    class Meta:
        model = AudioTableSettings
        exclude = []
