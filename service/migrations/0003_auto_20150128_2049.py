# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_auto_20150128_1936'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cost',
            options={'verbose_name_plural': 'Расходы', 'verbose_name': 'расходы'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Заявки', 'verbose_name': 'заявка'},
        ),
        migrations.AlterField(
            model_name='order',
            name='date_end',
            field=models.DateTimeField(blank=True, verbose_name='Время и дата выполнения заявки'),
            preserve_default=True,
        ),
    ]
