# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-11 07:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0008_auto_20171010_1019'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericObjectRelation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('related_audio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='media.Audio')),
                ('related_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='media.Image')),
                ('related_video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='media.Video')),
            ],
        ),
        migrations.CreateModel(
            name='RelationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='genericobjectrelation',
            name='relation_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='media.RelationType'),
        ),
        migrations.AddField(
            model_name='image',
            name='relation',
            field=models.ManyToManyField(to='media.GenericObjectRelation'),
        ),
    ]