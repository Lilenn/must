# Generated by Django 2.1.1 on 2018-09-27 03:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0002_auto_20180927_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 27, 11, 12, 53, 298924), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='programmodel',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 27, 11, 12, 53, 298924), verbose_name='更新时间'),
        ),
    ]
