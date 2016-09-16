# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('discografica', '0008_auto_20160428_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicacion',
            name='visitas',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
