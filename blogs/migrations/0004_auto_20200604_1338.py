# Generated by Django 2.2.3 on 2020-06-04 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20200604_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog_categories.BlogCategory'),
        ),
    ]
