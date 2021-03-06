# Generated by Django 2.1.1 on 2018-09-27 03:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 27, 11, 11, 16, 822783), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='programmodel',
            name='outline_id',
            field=models.IntegerField(default=0, verbose_name='一级大纲id'),
        ),
        migrations.AlterField(
            model_name='programmodel',
            name='stage_id',
            field=models.IntegerField(default=0, verbose_name='阶段id'),
        ),
        migrations.AlterField(
            model_name='programmodel',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 27, 11, 11, 16, 822783), verbose_name='更新时间'),
        ),
    ]
