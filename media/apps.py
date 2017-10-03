from __future__ import unicode_literals

from django.apps import AppConfig
from watson import search as watson


class MediaConfig(AppConfig):
    name = 'media'

    def ready(self):
        ImageModel = self.get_model("Image")
        watson.register(ImageModel)
        VideoModel = self.get_model("Video")
        watson.register(VideoModel)
