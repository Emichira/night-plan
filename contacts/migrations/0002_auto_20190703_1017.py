# Generated by Django 2.2 on 2019-07-03 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='user_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
