# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discografica', '0010_album_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='imagen',
            field=models.ImageField(upload_to='discografica/static/img/album', default='discografica/static/img/icon-face.png'),
        ),
    ]
