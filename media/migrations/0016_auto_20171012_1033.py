# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-12 08:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0015_audiotablesettings_videotablesettings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='audiotablesettings',
            old_name='show_created',
            new_name='audio_show_created',
        ),
        migrations.RenameField(
            model_name='audiotablesettings',
            old_name='show_description',
            new_name='audio_show_description',
        ),
        migrations.RenameField(
            model_name='audiotablesettings',
            old_name='show_filesize',
            new_name='audio_show_filesize',
        ),
        migrations.RenameField(
            model_name='audiotablesettings',
            old_name='show_length',
            new_name='audio_show_length',
        ),
        migrations.RenameField(
            model_name='audiotablesettings',
            old_name='show_modified',
            new_name='audio_show_modified',
        ),
        migrations.RenameField(
            model_name='audiotablesettings',
            old_name='show_path',
            new_name='audio_show_path',
        ),
        migrations.RenameField(
            model_name='audiotablesettings',
            old_name='show_preview',
            new_name='audio_show_preview',
        ),
        migrations.RenameField(
            model_name='audiotablesettings',
            old_name='show_rating',
            new_name='audio_show_rating',
        ),
        migrations.RenameField(
            model_name='audiotablesettings',
            old_name='show_relations',
            new_name='audio_show_relations',
        ),
        migrations.RenameField(
            model_name='audiotablesettings',
            old_name='show_tags',
            new_name='audio_show_tags',
        ),
        migrations.RenameField(
            model_name='audiotablesettings',
            old_name='show_type',
            new_name='audio_show_type',
        ),
        migrations.RenameField(
            model_name='imagetablesettings',
            old_name='show_created',
            new_name='image_show_created',
        ),
        migrations.RenameField(
            model_name='imagetablesettings',
            old_name='show_description',
            new_name='image_show_description',
        ),
        migrations.RenameField(
            model_name='imagetablesettings',
            old_name='show_filesize',
            new_name='image_show_filesize',
        ),
        migrations.RenameField(
            model_name='imagetablesettings',
            old_name='show_modified',
            new_name='image_show_modified',
        ),
        migrations.RenameField(
            model_name='imagetablesettings',
            old_name='show_path',
            new_name='image_show_path',
        ),
        migrations.RenameField(
            model_name='imagetablesettings',
            old_name='show_preview',
            new_name='image_show_preview',
        ),
        migrations.RenameField(
            model_name='imagetablesettings',
            old_name='show_rating',
            new_name='image_show_rating',
        ),
        migrations.RenameField(
            model_name='imagetablesettings',
            old_name='show_relations',
            new_name='image_show_relations',
        ),
        migrations.RenameField(
            model_name='imagetablesettings',
            old_name='show_size',
            new_name='image_show_size',
        ),
        migrations.RenameField(
            model_name='imagetablesettings',
            old_name='show_tags',
            new_name='image_show_tags',
        ),
        migrations.RenameField(
            model_name='imagetablesettings',
            old_name='show_type',
            new_name='image_show_type',
        ),
        migrations.RenameField(
            model_name='videotablesettings',
            old_name='show_created',
            new_name='video_show_created',
        ),
        migrations.RenameField(
            model_name='videotablesettings',
            old_name='show_description',
            new_name='video_show_description',
        ),
        migrations.RenameField(
            model_name='videotablesettings',
            old_name='show_filesize',
            new_name='video_show_filesize',
        ),
        migrations.RenameField(
            model_name='videotablesettings',
            old_name='show_length',
            new_name='video_show_length',
        ),
        migrations.RenameField(
            model_name='videotablesettings',
            old_name='show_modified',
            new_name='video_show_modified',
        ),
        migrations.RenameField(
            model_name='videotablesettings',
            old_name='show_path',
            new_name='video_show_path',
        ),
        migrations.RenameField(
            model_name='videotablesettings',
            old_name='show_preview',
            new_name='video_show_preview',
        ),
        migrations.RenameField(
            model_name='videotablesettings',
            old_name='show_rating',
            new_name='video_show_rating',
        ),
        migrations.RenameField(
            model_name='videotablesettings',
            old_name='show_relations',
            new_name='video_show_relations',
        ),
        migrations.RenameField(
            model_name='videotablesettings',
            old_name='show_tags',
            new_name='video_show_tags',
        ),
        migrations.RenameField(
            model_name='videotablesettings',
            old_name='show_type',
            new_name='video_show_type',
        ),
    ]
