# Generated by Django 2.2.3 on 2019-10-07 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0004_auto_20191007_0422'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='club',
            name='reservation_number',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
