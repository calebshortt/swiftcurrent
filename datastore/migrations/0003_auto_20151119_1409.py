# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datastore', '0002_auto_20151119_1334'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Crawlers',
            new_name='Crawler',
        ),
    ]
