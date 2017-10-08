from django.db import models
from tagulous.models import TagField, TagModel

import os
import time
from PIL import Image as pImg


class MediaTagModel(TagModel):
    class TagMeta:
        pass


CATEGORIES = [
    ('None', ""),
    ('Test', 'test'),
]


class MediaFile(models.Model):
    full_path = models.TextField(blank=False)
    is_deleted = models.BooleanField(default=False)
    category = models.TextField(blank=True, choices=CATEGORIES)

    class Meta:
        abstract = True

    @property
    def shortname(self):
        return os.path.split(os.path.splitext(self.full_path)[0])[-1]

    @property
    def path(self):
        return os.path.split(os.path.splitext(self.full_path)[0])[:-1][0]

    @property
    def filetype(self):
        return os.path.splitext(self.full_path)[-1]

    @property
    def filesize(self):
        return str(os.path.getsize(self.full_path)) + " KB"

    @property
    def last_modified_dt(self):
        # return time.ctime(os.path.getmtime(self.full_path))
        return time.ctime(os.path.getctime(self.full_path))

    @property
    def creation_dt(self):
        # return time.ctime(os.path.getctime(self.full_path))
        return time.ctime(os.path.getmtime(self.full_path))

    def __unicode__(self):
        return os.path.split(self.full_path)[-1]

    def __str__(self):
        return self.__unicode__()


class Image(MediaFile):
    tags = TagField(to=MediaTagModel)

    @property
    def image_size(self):
        im = pImg.open(self.full_path)
        return im.size


class Video(MediaFile):
    tags = TagField(to=MediaTagModel)


class Audio(MediaFile):
    tags = TagField(to=MediaTagModel)
