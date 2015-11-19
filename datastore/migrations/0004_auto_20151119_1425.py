# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datastore', '0003_auto_20151119_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sentiment',
            old_name='num_no',
            new_name='num_negative',
        ),
        migrations.RenameField(
            model_name='sentiment',
            old_name='num_yes',
            new_name='num_positive',
        ),
    ]
