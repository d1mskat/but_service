# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_auto_20150128_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('DO', 'В обработке'), ('OK', 'Выполнена')], max_length=2, verbose_name='Статус заявки'),
            preserve_default=True,
        ),
    ]
