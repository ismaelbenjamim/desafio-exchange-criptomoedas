from rest_framework import serializers


class CurrencyPairSerializer(serializers.Serializer):
    crypto = serializers.CharField()
    currencys = serializers.ListSerializer(child=serializers.CharField())
