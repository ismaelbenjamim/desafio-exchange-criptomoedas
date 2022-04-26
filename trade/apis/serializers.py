from rest_framework import serializers

from cryptocurrencies.models import Crypto
from trade.models import Trade
from users.models import User


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


class BuyCryptoIDSerializer(serializers.Serializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='uuid')
    id = serializers.SlugRelatedField(queryset=Trade.objects.all(), slug_field='id')
