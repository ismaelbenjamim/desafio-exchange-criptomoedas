# Generated by Django 3.1.14 on 2022-04-24 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('cryptocurrencies', '0004_cryptowallet_user_wallet'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cryptowallet',
            unique_together={('user_wallet', 'crypto')},
        ),
    ]