# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-04-25 09:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tweet', models.TextField()),
                ('polarity', models.IntegerField()),
                ('classifiedCorrectly', models.BooleanField()),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
