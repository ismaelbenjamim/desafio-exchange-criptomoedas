from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from cryptocurrencies.models import Crypto
from trade.models import Trade
from users.models import User, UserWallet


class SellCryptoSerializer(serializers.ModelSerializer):
    crypto = serializers.SlugRelatedField(queryset=Crypto.objects.all(), slug_field='abbreviation')
    class Meta:
        model = Trade
        fields = '__all__'


class BuyCryptoSerializer(serializers.ModelSerializer):
    crypto = serializers.SlugRelatedField(queryset=Crypto.objects.all(), slug_field='abbreviation')
    class Meta:
        model = Trade
        fields = '__all__'

    def validate(self, attrs):
        user_wallet = UserWallet.objects.get(user=attrs['buyer'])
        if attrs['price'] > user_wallet.balance:
            raise serializers.ValidationError({"buyer": "It's not possible because the price is bigger than the balance user"})
        return super(BuyCryptoSerializer, self).validate(attrs)


class BuyCryptoIDSerializer(serializers.Serializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='uuid')
    id = serializers.CharField(max_length=8, required=True)
