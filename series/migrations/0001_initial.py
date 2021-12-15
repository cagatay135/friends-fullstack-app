# Generated by Django 4.0 on 2021-12-13 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Makale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yazar', models.CharField(max_length=50)),
                ('baslik', models.CharField(max_length=100)),
                ('aciklama', models.CharField(max_length=200)),
                ('metin', models.TextField()),
                ('sehir', models.CharField(max_length=50)),
                ('aktif', models.BooleanField(default=True)),
                ('yaratilma_tarihi', models.DateTimeField(auto_now_add=True)),
                ('guncellenme_tarihi', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
