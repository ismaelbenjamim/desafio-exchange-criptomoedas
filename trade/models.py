import uuid as uuid
from django.db import models

from cryptocurrencies.models import Crypto, CryptoWallet
from users.models import User, UserWallet


class Trade(models.Model):
    STATUS_TRADE = (
        ('Available', 'Available'),
        ('Sold out', 'Sold out'),
        ('Canceled', 'Canceled')
    )
    uuid = models.UUIDField(verbose_name='UUID', primary_key=True, default=uuid.uuid4)
    status = models.CharField(verbose_name='Type', choices=STATUS_TRADE, max_length=20, default='Available')
    crypto = models.ForeignKey(Crypto, verbose_name='Crypto', on_delete=models.PROTECT)
    amount = models.DecimalField(verbose_name='Amount', max_digits=27, decimal_places=18, default=0)
    price = models.DecimalField(verbose_name='Price', max_digits=27, decimal_places=18, default=0)
    seller = models.ForeignKey(User, verbose_name='Seller', on_delete=models.PROTECT, related_name='Seller')
    buyer = models.ForeignKey(User, verbose_name='Buyer', on_delete=models.PROTECT, related_name='Buyer', null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.status == "Sold out":
            user_wallet_seller = UserWallet.objects.get(user=self.seller)
            user_wallet_seller.balance += self.price
            crypto_wallet_seller = CryptoWallet.objects.get(crypto=self.crypto, user_wallet=user_wallet_seller)
            crypto_wallet_seller.amount -= self.amount
            user_wallet_seller.save()
            crypto_wallet_seller.save()

            user_wallet_buyer = UserWallet.objects.get(user=self.buyer)
            user_wallet_buyer.balance -= self.price
            crypto_wallet_buyer = CryptoWallet.objects.get(crypto=self.crypto, user_wallet=user_wallet_buyer)
            crypto_wallet_buyer.amount += self.amount
            user_wallet_buyer.save()
            crypto_wallet_buyer.save()
        super(Trade, self).save(*args, **kwargs)
