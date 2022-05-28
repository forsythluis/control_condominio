# Generated by Django 4.0.2 on 2022-05-20 01:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pago_condominio', '0004_alter_pago_fecha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pago',
            name='fecha',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='fecha de pago'),
        ),
    ]
