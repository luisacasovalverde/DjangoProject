# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discografica', '0003_auto_20160428_0347'),
    ]

    operations = [
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
            name='Publicacion',
        ),
    ]
