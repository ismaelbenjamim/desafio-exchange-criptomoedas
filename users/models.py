import uuid as uuid
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    uuid = models.UUIDField(verbose_name='UUID', primary_key=True, default=uuid.uuid4)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.uuid})' if self.first_name and self.last_name \
            else str(self.email)


class UserWallet(models.Model):
    uuid = models.UUIDField(verbose_name='UUID', primary_key=True, default=uuid.uuid4)
    user = models.OneToOneField(User, verbose_name='Wallet owner', on_delete=models.CASCADE)
    balance = models.DecimalField(verbose_name='Balance USD', max_digits=27, decimal_places=18, default=0)

    def __str__(self):
        return str(self.user)
