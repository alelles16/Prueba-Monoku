# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodManager', '0002_inventario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventario',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
