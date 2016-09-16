# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discografica', '0006_auto_20160428_0503'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='publicacion',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='album',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='artista',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='cancion',
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Publicacion',
        ),
    ]
