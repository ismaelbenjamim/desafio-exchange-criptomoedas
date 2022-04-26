import uuid as uuid
from django.db import models

from users.models import UserWallet


class Crypto(models.Model):
    uuid = models.UUIDField(verbose_name='UUID', primary_key=True, default=uuid.uuid4)
    name = models.CharField(verbose_name='Name', unique=True, max_length=100)
    abbreviation = models.CharField(verbose_name='Abbreviation', max_length=10)
    description = models.CharField(verbose_name='Description', null=True, blank=True, max_length=200)
    active = models.BooleanField(verbose_name='Active', default=True)

    def __str__(self):
        return str(self.abbreviation)

    def save(self, *args, **kwargs):
        super(Crypto, self).save(*args, **kwargs)
        for user_wallet in UserWallet.objects.all():
            CryptoWallet.objects.get_or_create(
                user_wallet=user_wallet,
                crypto=Crypto.objects.get(uuid=self.uuid)
            )


class CryptoWallet(models.Model):
    uuid = models.UUIDField(verbose_name='UUID', primary_key=True, default=uuid.uuid4)
    user_wallet = models.ForeignKey(UserWallet, verbose_name='User Wallet', on_delete=models.CASCADE)
    crypto = models.ForeignKey(Crypto, verbose_name='Crypto', on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name='Amount', max_digits=27, decimal_places=18, default=0)

    class Meta:
        unique_together = ['user_wallet', 'crypto']

    def __str__(self):
        return f'{self.crypto.abbreviation} - {self.user_wallet.user}'
