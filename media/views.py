from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.core.exceptions import ObjectDoesNotExist
from django_propeller.views import NavBarMixin
from django.shortcuts import render
from django.http import HttpResponseRedirect

import os

from .navbars import MainNavBar, ImageContextNavBar, VideoContextBar, AudioContextBar, EmptyContextBar, \
    ReorganizeContextBar
from .media_settings import PATH, IMAGE_EXT, VIDEO_EXT, AUDIO_EXT
from .models import Image, Video, Audio, ImageTableSettings
from .forms import ImageTableSettingsForm


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
    for img in Image.objects.all():
        if not img.exists:
            img.delete()
    for vid in Video.objects.all():
        if not vid.exists:
            vid.delete()
    for aud in Audio.objects.all():
        if not aud.exists:
            aud.delete()
    images = Image.objects.all()
    videos = Video.objects.all()
    audio = Audio.objects.all()
    return {'images': images, 'videos': videos, 'audio': audio}


class MainNavView(TemplateView, NavBarMixin):
    navbar_class = MainNavBar


class IndexPage(MainNavView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainNavView, self).get_context_data(**kwargs)
        context['context_bar'] = EmptyContextBar()
        return context


class ImagePage(MainNavView):
    template_name = 'images.html'

    def get_context_data(self, **kwargs):
        context = super(MainNavView, self).get_context_data(**kwargs)
        context['media'] = get_media()
        context['context_bar'] = ImageContextNavBar()
        context['table_settings'] = ImageTableSettings.objects.all()[0]
        return context


class VideoPage(MainNavView):
    template_name = 'videos.html'

    def get_context_data(self, **kwargs):
        context = super(MainNavView, self).get_context_data(**kwargs)
        context['media'] = get_media()
        context['context_bar'] = VideoContextBar()
        return context


class AudioPage(MainNavView):
    template_name = 'audio.html'

    def get_context_data(self, **kwargs):
        context = super(MainNavView, self).get_context_data(**kwargs)
        context['media'] = get_media()
        context['context_bar'] = AudioContextBar()
        return context


def settings(request):
    if request.method == 'POST':
        form = ImageTableSettingsForm(request.POST)
        if form.is_valid():
            _settings = ImageTableSettings.objects.get_or_create(id=1)[0]
            _settings.show_preview = form.cleaned_data['show_preview']
            _settings.show_description = form.cleaned_data['show_description']
            _settings.show_type = form.cleaned_data['show_type']
            _settings.show_size = form.cleaned_data['show_size']
            _settings.show_path = form.cleaned_data['show_path']
            _settings.show_filesize = form.cleaned_data['show_filesize']
            _settings.show_modified = form.cleaned_data['show_modified']
            _settings.show_created = form.cleaned_data['show_created']
            _settings.show_rating = form.cleaned_data['show_rating']
            _settings.show_tags = form.cleaned_data['show_tags']
            _settings.show_relations = form.cleaned_data['show_relations']
            _settings.save()
            return HttpResponseRedirect('/settings/')
    else:
        form = ImageTableSettingsForm(instance=ImageTableSettings.objects.get_or_create(id=1)[0])

    return render(request, 'settings.html', {'form': form, 'context_bar': EmptyContextBar(), 'navbar': MainNavBar()})


class ReorganizePage(MainNavView):
    template_name = 'reorganize.html'

    def get_context_data(self, **kwargs):
        context = super(MainNavView, self).get_context_data(**kwargs)
        context['context_bar'] = ReorganizeContextBar(kwargs.get('page-context', ''))
        return context
