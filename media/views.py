from django.views.generic.base import TemplateView
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django_propeller.views import NavBarMixin
from django_ajax.decorators import ajax
from django.conf import settings as dj_settings

import os

from .navbars import MainNavBar, ImageContextNavBar, VideoContextBar, AudioContextBar, EmptyContextBar, \
    ReorganizeContextBar
from .media_settings import PATH, IMAGE_EXT, VIDEO_EXT, AUDIO_EXT
from .models import Image, Video, Audio, ImageTableSettings, VideoTableSettings, AudioTableSettings, Category
from .forms import ImageTableSettingsForm, VideoTableSettingsForm, AudioTableSettingsForm


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
        if ImageTableSettings.objects.count() > 0:
            context['table_settings'] = ImageTableSettings.objects.all()[0]
        return context


class VideoPage(MainNavView):
    template_name = 'videos.html'

    def get_context_data(self, **kwargs):
        context = super(MainNavView, self).get_context_data(**kwargs)
        context['media'] = get_media()
        context['context_bar'] = VideoContextBar()
        if VideoTableSettings.objects.count() > 0:
            context['table_settings'] = VideoTableSettings.objects.all()[0]
        return context


class AudioPage(MainNavView):
    template_name = 'audio.html'

    def get_context_data(self, **kwargs):
        context = super(MainNavView, self).get_context_data(**kwargs)
        context['media'] = get_media()
        context['context_bar'] = AudioContextBar()
        if AudioTableSettings.objects.count() > 0:
            context['table_settings'] = AudioTableSettings.objects.all()[0]
        return context


def settings(request):
    if request.method == 'POST':
        image_table_form = ImageTableSettingsForm(request.POST)
        if image_table_form.is_valid():
            _settings = ImageTableSettings.objects.get_or_create(id=1)[0]
            _settings.show_preview = image_table_form.cleaned_data['image_show_preview']
            _settings.show_description = image_table_form.cleaned_data['image_show_description']
            _settings.show_type = image_table_form.cleaned_data['image_show_type']
            _settings.show_size = image_table_form.cleaned_data['image_show_size']
            _settings.show_path = image_table_form.cleaned_data['image_show_path']
            _settings.show_filesize = image_table_form.cleaned_data['image_show_filesize']
            _settings.show_modified = image_table_form.cleaned_data['image_show_modified']
            _settings.show_created = image_table_form.cleaned_data['image_show_created']
            _settings.show_rating = image_table_form.cleaned_data['image_show_rating']
            _settings.show_tags = image_table_form.cleaned_data['image_show_tags']
            _settings.show_relations = image_table_form.cleaned_data['image_show_relations']
            _settings.save()
        video_table_form = VideoTableSettingsForm(request.POST)
        if video_table_form.is_valid():
            _settings = VideoTableSettings.objects.get_or_create(id=1)[0]
            _settings.show_preview = video_table_form.cleaned_data['video_show_preview']
            _settings.show_description = video_table_form.cleaned_data['video_show_description']
            _settings.show_type = video_table_form.cleaned_data['video_show_type']
            _settings.show_length = video_table_form.cleaned_data['video_show_length']
            _settings.show_path = video_table_form.cleaned_data['video_show_path']
            _settings.show_filesize = video_table_form.cleaned_data['video_show_filesize']
            _settings.show_modified = video_table_form.cleaned_data['video_show_modified']
            _settings.show_created = video_table_form.cleaned_data['video_show_created']
            _settings.show_rating = video_table_form.cleaned_data['video_show_rating']
            _settings.show_tags = video_table_form.cleaned_data['video_show_tags']
            _settings.show_relations = video_table_form.cleaned_data['video_show_relations']
            _settings.save()
        audio_table_form = AudioTableSettingsForm(request.POST)
        if audio_table_form.is_valid():
            _settings = AudioTableSettings.objects.get_or_create(id=1)[0]
            _settings.show_preview = audio_table_form.cleaned_data['audio_show_preview']
            _settings.show_description = audio_table_form.cleaned_data['audio_show_description']
            _settings.show_type = audio_table_form.cleaned_data['audio_show_type']
            _settings.show_length = audio_table_form.cleaned_data['audio_show_length']
            _settings.show_path = audio_table_form.cleaned_data['audio_show_path']
            _settings.show_filesize = audio_table_form.cleaned_data['audio_show_filesize']
            _settings.show_modified = audio_table_form.cleaned_data['audio_show_modified']
            _settings.show_created = audio_table_form.cleaned_data['audio_show_created']
            _settings.show_rating = audio_table_form.cleaned_data['audio_show_rating']
            _settings.show_tags = audio_table_form.cleaned_data['audio_show_tags']
            _settings.show_relations = audio_table_form.cleaned_data['audio_show_relations']
            _settings.save()
        return HttpResponseRedirect('/settings/')
    else:
        image_table_form = ImageTableSettingsForm(instance=ImageTableSettings.objects.get_or_create(id=1)[0])
        video_table_form = VideoTableSettingsForm(instance=VideoTableSettings.objects.get_or_create(id=1)[0])
        audio_table_form = AudioTableSettingsForm(instance=AudioTableSettings.objects.get_or_create(id=1)[0])

    return render(request, 'settings.html', {
        'image_table_form': image_table_form,
        'video_table_form': video_table_form,
        'audio_table_form': audio_table_form,
        'context_bar': EmptyContextBar(),
        'navbar': MainNavBar()
    })


class ReorganizePage(MainNavView):
    template_name = 'reorganize.html'

    def get_context_data(self, **kwargs):
        context = super(MainNavView, self).get_context_data(**kwargs)
        context['context_bar'] = ReorganizeContextBar(kwargs.get('page-context', ''))
        context['page_context'] = kwargs.get('page-context', '').lower()
        return context


@ajax
def organize_structure(request):
    context = request.GET.get('pcon')
    pattern = request.GET.get('pattern')
    bpath = dj_settings.MEDIA_ROOT
    categories = Category.objects.all()
    if context == 'images':
        if pattern == 'cat-as-sub':
            try:
                for cat in categories:
                    images = Image.objects.filter(category=cat)
                    if images.count() > 0:
                        cat_path = os.path.join(bpath, cat.name)
                        if not os.path.exists(cat_path):
                            os.mkdir(cat_path)
                        for img in images:
                            old_path = img.full_path
                            new_path = os.path.join(cat_path, img.shortname + img.filetype)
                            os.rename(old_path, new_path)
            except Exception as e:
                print(e)
        return HttpResponseRedirect('/images/')
    return HttpResponseRedirect('/')
