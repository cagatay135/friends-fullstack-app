# Generated by Django 4.0 on 2021-12-13 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0005_remove_episode_quotes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='number_episode',
            field=models.PositiveIntegerField(),
        ),
    ]
