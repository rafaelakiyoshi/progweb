# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 19:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='text',
            field=models.TextField(default='Página de texto padrão'),
            preserve_default=False,
        ),
    ]
