# Generated by Django 2.1.7 on 2019-03-05 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_repair_shop', '0003_auto_20190305_1437'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='secondmaster',
            options={'verbose_name': 'Запись к 2 мастеру', 'verbose_name_plural': 'Записи к 2 мастеру'},
        ),
        migrations.AlterField(
            model_name='firstmaster',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 5, 16, 28, 59, 853899), verbose_name='Время и дата записи'),
        ),
        migrations.AlterField(
            model_name='secondmaster',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 5, 16, 28, 59, 854649), verbose_name='Время и дата записи'),
        ),
        migrations.AlterField(
            model_name='thirdmaster',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 5, 16, 28, 59, 855323), verbose_name='Время и дата записи'),
        ),
    ]