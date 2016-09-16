# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('discografica', '0007_auto_20160428_0612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('fecha', models.PositiveSmallIntegerField()),
                ('artista', models.ForeignKey(to='discografica.Artista')),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('upload_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('album', models.ForeignKey(to='discografica.Album')),
                ('cancion', models.ForeignKey(to='discografica.Cancion')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='publicacion',
            unique_together=set([('album', 'cancion')]),
        ),
    ]
