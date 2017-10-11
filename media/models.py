from django.db import models
from tagulous.models import TagField, TagModel

import os
import time
from PIL import Image as pImg


class MediaTagModel(TagModel):
    class TagMeta:
        pass


class RelationType(models.Model):
    text = models.CharField(max_length=60, blank=False)

    def __unicode__(self):
        return self.text

    def __str__(self):
        return self.text


class GenericObjectRelation(models.Model):
    relation_type = models.ForeignKey(RelationType)
    related_image = models.ManyToManyField('Image', blank=True)
    related_video = models.ManyToManyField('Video', blank=True)
    related_audio = models.ManyToManyField('Audio', blank=True)

    @property
    def related_images(self):
        if self.related_image.count() > 0:
            return "Images:" + ", ".join([x.get_link for x in self.related_image.all()])
        return ""

    @property
    def related_videos(self):
        if self.related_video.count() > 0:
            return "Videos:" + ", ".join([x.get_link for x in self.related_video.all()])
        return ""

    @property
    def related_audios(self):
        if self.related_audio.count() > 0:
            return "Audio:" + ", ".join([x.get_link for x in self.related_audio.all()])
        return ""

    def __unicode__(self):
        return self.relation_type.text + ": [" + self.related_images + "\n"\
               + self.related_videos + "\n" + self.related_audios + "]"

    def __str__(self):
        return self.relation_type.text + ": [" + self.related_images + "\n" \
               + self.related_videos + "\n" + self.related_audios + "]"


class Category(models.Model):
    name = models.CharField(max_length=60)

    @property
    def as_choice(self):
        return self.name, self.name.lower()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class MediaFile(models.Model):
    full_path = models.TextField(blank=False)
    is_deleted = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True

    @property
    def exists(self):
        return os.path.exists(self.full_path)

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

    @property
    def get_link(self):
        return "<a href='/media/%s'>%s</a>" % (os.path.split(self.full_path)[-1], self.shortname)

    def __unicode__(self):
        return os.path.split(self.full_path)[-1]

    def __str__(self):
        return os.path.split(self.full_path)[-1]


class Image(MediaFile):
    tags = TagField(to=MediaTagModel, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    relation = models.ManyToManyField(GenericObjectRelation, blank=True)

    @property
    def categories(self):
        return ",".join([x.name for x in self.category.all()])

    @property
    def image_size(self):
        im = pImg.open(self.full_path)
        return im.size

    def get_relations(self):
        return "\n".join([str(x) for x in self.relation.all()])


class Video(MediaFile):
    tags = TagField(to=MediaTagModel, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    relation = models.ManyToManyField(GenericObjectRelation, blank=True)

    @property
    def categories(self):
        return ",".join([x.name for x in self.category.all()])

    def get_relations(self):
        return "\n".join([str(x) for x in self.relation.all()])


class Audio(MediaFile):
    tags = TagField(to=MediaTagModel, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    relation = models.ManyToManyField(GenericObjectRelation, blank=True)

    @property
    def categories(self):
        return ",".join([x.name for x in self.category.all()])

    def get_relations(self):
        return "\n".join([str(x) for x in self.relation.all()])


class ImageTableSettings(models.Model):
    show_preview = models.BooleanField(default=True)
    show_description = models.BooleanField(default=True)
    show_type = models.BooleanField(default=True)
    show_size = models.BooleanField(default=True)
    show_path = models.BooleanField(default=True)
    show_filesize = models.BooleanField(default=True)
    show_modified = models.BooleanField(default=True)
    show_created = models.BooleanField(default=True)
    show_rating = models.BooleanField(default=True)
    show_tags = models.BooleanField(default=True)
    show_relations = models.BooleanField(default=True)
