# Generated by Django 2.1.1 on 2018-09-26 03:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0006_auto_20180926_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 11, 42, 39, 528824)),
        ),
        migrations.AlterField(
            model_name='subjectmodel',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 26, 11, 42, 39, 528824)),
        ),
    ]
