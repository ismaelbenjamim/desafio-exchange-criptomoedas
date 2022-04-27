import uuid as uuid

from django.core.exceptions import ValidationError
from django.db import models

from core.functions import generate_trade_id, validate_unique_id_trade, validate_main_sequence_trade
from cryptocurrencies.models import Crypto, CryptoWallet
from users.models import User, UserWallet


class Trade(models.Model):
    STATUS_TRADE = (
        ('Available', 'Available'),
        ('Sold out', 'Sold out'),
        ('Canceled', 'Canceled')
    )
    uuid = models.UUIDField(verbose_name='UUID', primary_key=True, default=uuid.uuid4)
    id = models.CharField(verbose_name='Trade ID', default=generate_trade_id, max_length=8)
    status = models.CharField(verbose_name='Type', choices=STATUS_TRADE, max_length=20, default='Available')
    closed = models.BooleanField(verbose_name='Closed trade', default=False)
    crypto = models.ForeignKey(Crypto, verbose_name='Crypto', on_delete=models.CASCADE)
    amount = models.DecimalField(verbose_name='Amount', max_digits=27, decimal_places=18, default=0)
    price = models.DecimalField(verbose_name='Price', max_digits=27, decimal_places=18, default=0)
    seller = models.ForeignKey(User, verbose_name='Seller', on_delete=models.CASCADE, related_name='Seller')
    buyer = models.ForeignKey(User, verbose_name='Buyer', on_delete=models.CASCADE, related_name='Buyer', null=True, blank=True)
    date = models.DateTimeField(verbose_name='Date', auto_now_add=True)
    main = models.BooleanField(verbose_name='Main trade of sequence', default=False)
    root = models.ForeignKey('Trade', verbose_name='Trade history', on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        if self.status == "Sold out" and self.closed:
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
            self.closed = True
        super(Trade, self).save(*args, **kwargs)
        
    def clean(self):
        super(Trade, self).validate_unique()
        errors = {}

        validate_main = validate_main_sequence_trade(self.uuid, self.id, self.main)
        if validate_main:
            errors['main'] = validate_main

        validate_id = validate_unique_id_trade(self.uuid, self.id, self.seller,
                                               self.crypto, self.amount, self.price, self.root)
        if validate_id:
            errors['id'] = validate_id

        if errors:
            raise ValidationError(errors)
