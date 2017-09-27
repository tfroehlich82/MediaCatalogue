from django.views.generic.base import TemplateView
from django_propeller.views import NavBarMixin

import os

from .navbars import MainNavBar
from .media_settings import PATH, IMAGE_EXT


def get_media():
    all_files = os.listdir(PATH)
    images = []
    for itm in all_files:
        ext = os.path.splitext(itm)
        if ext[-1].lower() in IMAGE_EXT:
            images.append(itm)
    return {'images': images, 'path': PATH}


class MainNavView(TemplateView, NavBarMixin):
    navbar_class = MainNavBar

    def get_context_data(self, **kwargs):
        context = super(MainNavView, self).get_context_data(**kwargs)
        all_media = get_media()
        context['media'] = all_media
        return context


class IndexPage(MainNavView):
    template_name = 'index.html'
