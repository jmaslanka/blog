# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-10 19:47
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import stdimage.models
import stdimage.utils
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taggit', '0002_auto_20150616_2121'),
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=224, verbose_name='title')),
                ('slug', models.SlugField(max_length=255, verbose_name='slug')),
                ('is_public', models.BooleanField(default=False, verbose_name='is public')),
                ('publication_date', models.DateTimeField(blank=True, null=True, verbose_name='publication date')),
                ('image', stdimage.models.StdImageField(blank=True, upload_to=stdimage.utils.UploadToUUID(path='articles'))),
                ('description', models.TextField(max_length=255, verbose_name='description')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to=settings.AUTH_USER_MODEL, verbose_name='author')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
            },
            managers=[
                ('published', django.db.models.manager.Manager()),
            ],
        ),
    ]
