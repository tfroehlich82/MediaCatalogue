from django.db import models
from tagulous.models import TagField
import os


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


class Image(MediaFile):
    tags = TagField()

    def __init__(self, *args, **kwargs):
        super(Image, self).__init__(*args, **kwargs)
