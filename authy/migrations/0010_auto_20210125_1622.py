# Generated by Django 3.0.5 on 2021-01-25 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0009_profile_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='full_name',
        ),
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
