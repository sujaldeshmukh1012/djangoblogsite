# Generated by Django 3.0.5 on 2021-01-24 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0010_auto_20210124_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(default='Post Title'),
        ),
    ]