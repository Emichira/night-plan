# Generated by Django 2.2 on 2019-06-27 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counties', '0002_county_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='county',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
