# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cantidadActual', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('producto', models.ForeignKey(to='foodManager.Producto')),
            ],
        ),
    ]
