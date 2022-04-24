# Generated by Django 3.1.14 on 2022-04-24 07:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cryptocurrencies', '0005_auto_20220424_0044'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='UUID')),
                ('status', models.CharField(choices=[('Available', 'Available'), ('Sold out', 'Sold out'), ('Canceled', 'Canceled')], default='Available', max_length=20, verbose_name='Type')),
                ('amount', models.DecimalField(decimal_places=18, default=0, max_digits=27, verbose_name='Amount')),
                ('price', models.DecimalField(decimal_places=18, default=0, max_digits=27, verbose_name='Price')),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Buyer', to=settings.AUTH_USER_MODEL, verbose_name='Buyer')),
                ('crypto', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cryptocurrencies.crypto', verbose_name='Crypto')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Seller', to=settings.AUTH_USER_MODEL, verbose_name='Seller')),
            ],
        ),
    ]
