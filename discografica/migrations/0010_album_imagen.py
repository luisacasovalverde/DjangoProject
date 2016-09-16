# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discografica', '0009_publicacion_visitas'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='imagen',
            field=models.ImageField(upload_to='static/img/album', default='static/img/icon-face.png'),
        ),
    ]
