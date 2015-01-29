# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_end',
            field=models.DateTimeField(verbose_name='Время и дата выполнения заявки'),
            preserve_default=True,
        ),
    ]
