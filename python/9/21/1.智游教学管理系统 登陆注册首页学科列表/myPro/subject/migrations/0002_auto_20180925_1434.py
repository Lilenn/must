# Generated by Django 2.1.1 on 2018-09-25 06:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjectmodel',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 25, 14, 34, 32, 873329)),
        ),
        migrations.AlterField(
            model_name='subjectmodel',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 25, 14, 34, 32, 873329)),
        ),
    ]
