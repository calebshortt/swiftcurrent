# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crawlers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_address', models.IPAddressField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sentiment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255, blank=True)),
                ('num_yes', models.IntegerField(default=0)),
                ('num_no', models.IntegerField(default=0)),
                ('num_neutral', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='TextRelations',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rel_from', models.ForeignKey(related_name='rel_from', to='datastore.Sentiment')),
                ('rel_to', models.ForeignKey(related_name='rel_to', to='datastore.Sentiment')),
            ],
        ),
    ]
