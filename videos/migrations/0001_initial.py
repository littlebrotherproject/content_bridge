# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('message_id', models.CharField(max_length=20)),
                ('from_address', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('recieved', models.DateTimeField()),
                ('text_body', models.TextField()),
                ('html_body', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('youtube_id', models.CharField(max_length=11)),
                ('title', models.CharField(max_length=200, null=True)),
                ('published', models.DateTimeField(null=True)),
                ('duration', models.IntegerField(null=True)),
                ('thumbnail', models.URLField(max_length=20, null=True)),
                ('email', models.OneToOneField(null=True, to='videos.Email')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
