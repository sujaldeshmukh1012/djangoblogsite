# Generated by Django 3.0.7 on 2020-07-11 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_likes'),
        ('authy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='favorites',
            field=models.ManyToManyField(to='post.Post'),
        ),
    ]
