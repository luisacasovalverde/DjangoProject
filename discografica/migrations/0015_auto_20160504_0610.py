# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discografica', '0014_auto_20160504_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='imagen',
            field=models.ImageField(default='discografica/static/img/icon-face.png', upload_to='discografica/static/img/album'),
        ),
    ]
