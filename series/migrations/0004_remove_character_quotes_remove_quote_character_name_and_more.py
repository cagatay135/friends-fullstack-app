# Generated by Django 4.0 on 2021-12-13 22:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0003_alter_character_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='quotes',
        ),
        migrations.RemoveField(
            model_name='quote',
            name='character_name',
        ),
        migrations.AddField(
            model_name='quote',
            name='character',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='series.character'),
            preserve_default=False,
        ),
    ]
