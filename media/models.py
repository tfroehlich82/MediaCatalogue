from django.db import models
from tagulous.models import TagField, TagModel
import os


class MediaTagModel(TagModel):
    class TagMeta:
        pass


class MediaFile(models.Model):
    full_path = models.TextField(blank=False)
    is_deleted = models.BooleanField(default=False)

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

    def __unicode__(self):
        return os.path.split(self.full_path)[-1]

    def __str__(self):
        return self.__unicode__()


class Image(MediaFile):
    tags = TagField(to=MediaTagModel)


class Video(MediaFile):
    tags = TagField(to=MediaTagModel)


class Audio(MediaFile):
    tags = TagField(to=MediaTagModel)
