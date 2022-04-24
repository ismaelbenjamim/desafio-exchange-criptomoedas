from django.contrib import admin

from cryptocurrencies.models import Crypto, CryptoWallet

admin.site.register(Crypto)
admin.site.register(CryptoWallet)
