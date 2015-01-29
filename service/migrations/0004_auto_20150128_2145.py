# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_auto_20150128_2049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='order_no',
            field=models.ForeignKey(verbose_name='Расходы по заявке', to='service.Order'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cost',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Цель расходов'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cost',
            name='total_price',
            field=models.DecimalField(decimal_places=2, max_digits=19, verbose_name='Общая стоимость (грн)'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='date_end',
            field=models.DateTimeField(blank=True, verbose_name='Время и дата выполнения заявки', null=True),
            preserve_default=True,
        ),
    ]
