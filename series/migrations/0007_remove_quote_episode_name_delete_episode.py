# Generated by Django 4.0 on 2021-12-13 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0006_alter_character_number_episode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='episode_name',
        ),
        migrations.DeleteModel(
            name='Episode',
        ),
    ]