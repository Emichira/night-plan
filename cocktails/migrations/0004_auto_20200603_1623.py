# Generated by Django 2.2.3 on 2020-06-03 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktails', '0003_auto_20200603_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='block_quote',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]