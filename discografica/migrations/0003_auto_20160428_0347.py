# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discografica', '0002_publicacion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publicacion',
            old_name='id_album',
            new_name='album',
        ),
        migrations.RenameField(
            model_name='publicacion',
            old_name='id_artista',
            new_name='artista',
        ),
        migrations.RenameField(
            model_name='publicacion',
            old_name='id_cancion',
            new_name='cancion',
        ),
    ]
