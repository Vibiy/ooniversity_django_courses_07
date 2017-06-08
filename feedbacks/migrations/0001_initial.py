# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-07 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='имя отправителя')),
                ('subject', models.CharField(max_length=255, verbose_name='тема сообщения')),
                ('message', models.TextField(verbose_name='само сообщение')),
                ('from_email', models.EmailField(max_length=254, verbose_name='email отправителя')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='дата и время создания')),
            ],
        ),
    ]
