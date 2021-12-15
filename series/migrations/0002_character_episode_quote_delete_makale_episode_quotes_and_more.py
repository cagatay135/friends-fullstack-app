# Generated by Django 4.0 on 2021-12-13 22:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('series', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Male', 'male'), ('Female', 'female')], max_length=50)),
                ('number_episode', models.PositiveBigIntegerField()),
                ('portrayed_by', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('season', models.PositiveSmallIntegerField()),
                ('number_episode', models.PositiveSmallIntegerField()),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('character_name', models.CharField(max_length=50)),
                ('episode_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='series.episode')),
            ],
        ),
        migrations.DeleteModel(
            name='Makale',
        ),
        migrations.AddField(
            model_name='episode',
            name='quotes',
            field=models.ManyToManyField(to='series.Quote'),
        ),
        migrations.AddField(
            model_name='character',
            name='quotes',
            field=models.ManyToManyField(to='series.Quote'),
        ),
    ]