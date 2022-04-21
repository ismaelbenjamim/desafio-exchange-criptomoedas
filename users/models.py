from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class UserWallet(models.Model):
    user = models.OneToOneField(User, verbose_name='Wallet owner', on_delete=models.CASCADE)
    balance = models.DecimalField(verbose_name='Balance', max_digits=27, decimal_places=18, default=0)
    bitcoins = models.DecimalField(verbose_name='BTC', max_digits=27, decimal_places=18, default=0)
    ethereus = models.DecimalField(verbose_name='ETH', max_digits=27, decimal_places=18, default=0)
    litecoins = models.DecimalField(verbose_name='LTC', max_digits=27, decimal_places=18, default=0)
