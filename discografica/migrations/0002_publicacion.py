# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('discografica', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('id_album', models.ManyToManyField(to='discografica.Album')),
                ('id_artista', models.ManyToManyField(to='discografica.Artista')),
                ('id_cancion', models.ManyToManyField(to='discografica.Cancion')),
            ],
        ),
    ]
