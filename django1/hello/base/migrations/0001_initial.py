# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=45)),
                ('password', models.CharField(max_length=40)),
                ('cookie_count', models.IntegerField()),
                ('created', models.DateTimeField()),
            ],
        ),
    ]
