# Generated by Django 3.0.7 on 2021-01-27 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0013_auto_20210126_2244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='caption',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='Text'),
        ),
    ]
