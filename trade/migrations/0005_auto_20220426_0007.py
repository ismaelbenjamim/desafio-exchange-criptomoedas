# Generated by Django 3.1.14 on 2022-04-26 03:07

import core.functions
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trade', '0004_auto_20220425_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trade',
            name='main',
            field=models.BooleanField(default=True, validators=[core.functions.validate_main_sequence_trade], verbose_name='Main trade of sequence'),
        ),
    ]