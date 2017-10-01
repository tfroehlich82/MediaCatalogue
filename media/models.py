from django.db import models
import os
from taggit.managers import TaggableManager


class MediaFile(models.Model):
    full_path = models.TextField(blank=False)
    is_deleted = models.BooleanField(default=False)
    # tags = TaggableManager()

    class Meta:
        abstract = True

    @property
    def shortname(self):
        return os.path.splitext(self.full_path)[0]

    @property
    def filetype(self):
        return os.path.splitext(self.full_path)[-1]


class Image(MediaFile):

    def __init__(self, filepath, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)

        self.full_path = filepath
