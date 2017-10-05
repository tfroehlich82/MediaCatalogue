from django.views.generic.base import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django_propeller.views import NavBarMixin

import os

from .navbars import MainNavBar
from .media_settings import PATH, IMAGE_EXT, VIDEO_EXT, AUDIO_EXT
from .models import Image, Video, Audio


def get_media():
    all_files = os.listdir(PATH)
    for itm in all_files:
        ext = os.path.splitext(itm)
        if ext[-1].lower() in IMAGE_EXT:
            full_path = os.path.join(PATH, itm)
            try:
                Image.objects.get(full_path=full_path)
            except ObjectDoesNotExist:
                img = Image()
                img.full_path = full_path
                img.save()
        elif ext[-1].lower() in VIDEO_EXT:
            full_path = os.path.join(PATH, itm)
            try:
                Video.objects.get(full_path=full_path)
            except ObjectDoesNotExist:
                vid = Video()
                vid.full_path = full_path
                vid.save()
        elif ext[-1].lower() in AUDIO_EXT:
            full_path = os.path.join(PATH, itm)
            try:
                Audio.objects.get(full_path=full_path)
            except ObjectDoesNotExist:
                aud = Audio()
                aud.full_path = full_path
                aud.save()
    images = Image.objects.all()
    videos = Video.objects.all()
    audio = Audio.objects.all()
    return {'images': images, 'videos': videos, 'audio': audio}


class MainNavView(TemplateView, NavBarMixin):
    navbar_class = MainNavBar

    def get_context_data(self, **kwargs):
        context = super(MainNavView, self).get_context_data(**kwargs)
        all_media = get_media()
        context['media'] = all_media
        return context


class IndexPage(MainNavView):
    template_name = 'index.html'


class ImagePage(MainNavView):
    template_name = 'images.html'


class VideoPage(MainNavView):
    template_name = 'videos.html'


class AudioPage(MainNavView):
    template_name = 'audio.html'


class SettingsPage(MainNavView):
    template_name = 'settings.html'
