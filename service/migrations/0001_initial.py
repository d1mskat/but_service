# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('total_price', models.DecimalField(max_digits=19, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('phone', models.CharField(max_length=16, verbose_name='Телефон')),
                ('status', models.CharField(max_length=25, verbose_name='Статус заявки')),
                ('breaking_type', models.CharField(max_length=255, verbose_name='Тип поломки')),
                ('date_added', models.DateTimeField(verbose_name='Время и дата создания заявки')),
                ('date_end', models.DateTimeField(verbose_name='Время и дата выполнения заявки', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cost',
            name='order_no',
            field=models.ForeignKey(to='service.Order'),
            preserve_default=True,
        ),
    ]
