# Generated by Django 2.2 on 2019-06-07 18:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20190606_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_end_date',
            field=models.TimeField(default=datetime.datetime.now),
        ),
    ]
