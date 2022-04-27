import uuid as uuid

from django.apps import apps
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models


class User(AbstractUser):
    uuid = models.UUIDField(verbose_name='UUID', primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.uuid})' if self.first_name and self.last_name \
            else str(self.email)

    def clean(self):
        self.password = make_password(self.password)
        super(User, self).clean()

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        UserWallet.objects.get_or_create(
            user=User.objects.get(uuid=self.uuid)
        )


class UserWallet(models.Model):
    uuid = models.UUIDField(verbose_name='UUID', primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(User, verbose_name='Wallet owner', on_delete=models.CASCADE)
    balance = models.DecimalField(verbose_name='Balance USD', max_digits=27, decimal_places=18, default=0)

    def __str__(self):
        return str(self.user)

    def clean(self):
        errors = {}

        if self.balance < 0:
            errors['balance'] = "It's not possible beacuse the value balance need is bigger zero"

        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        self.full_clean()
        super(UserWallet, self).save(*args, **kwargs)
        cryptos = apps.get_model(app_label='cryptocurrencies', model_name='Crypto')
        cryptowallet = apps.get_model(app_label='cryptocurrencies', model_name='CryptoWallet')
        for crypto in cryptos.objects.all():
            cryptowallet.objects.get_or_create(
                user_wallet=UserWallet.objects.get(uuid=self.uuid),
                crypto=crypto
            )
