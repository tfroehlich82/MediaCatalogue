# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-11 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0013_auto_20171011_1014'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageTableSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_preview', models.BooleanField(default=True)),
                ('show_description', models.BooleanField(default=True)),
                ('show_type', models.BooleanField(default=True)),
                ('show_size', models.BooleanField(default=True)),
                ('show_path', models.BooleanField(default=True)),
                ('show_filesize', models.BooleanField(default=True)),
                ('show_modified', models.BooleanField(default=True)),
                ('show_created', models.BooleanField(default=True)),
                ('show_rating', models.BooleanField(default=True)),
                ('show_tags', models.BooleanField(default=True)),
                ('show_relations', models.BooleanField(default=True)),
            ],
        ),
    ]
