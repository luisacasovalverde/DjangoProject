# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('discografica', '0004_auto_20160428_0416'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('album', models.ForeignKey(to='discografica.Album')),
                ('artista', models.ForeignKey(to='discografica.Artista')),
                ('cancion', models.ForeignKey(to='discografica.Cancion')),
            ],
        ),
    ]
