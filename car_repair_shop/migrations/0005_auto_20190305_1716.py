# Generated by Django 2.1.7 on 2019-03-05 17:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_repair_shop', '0004_auto_20190305_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firstmaster',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 5, 17, 16, 37, 107196), verbose_name='Время и дата записи'),
        ),
        migrations.AlterField(
            model_name='secondmaster',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 5, 17, 16, 37, 108063), verbose_name='Время и дата записи'),
        ),
        migrations.AlterField(
            model_name='thirdmaster',
            name='register_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 5, 17, 16, 37, 108714), verbose_name='Время и дата записи'),
        ),
    ]
