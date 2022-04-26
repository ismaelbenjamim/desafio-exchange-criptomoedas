from rest_framework import serializers

from users.models import User, UserWallet


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['uuid', 'username', 'email', 'first_name', 'last_name']


class UserBalanceSerializer(serializers.Serializer):
    uuid = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='uuid')


class UserWalletSerializer(serializers.Serializer):
    user = serializers.SlugRelatedField(queryset=UserWallet.objects.all(), slug_field='uuid')
    crypto_in_usd = serializers.BooleanField(default=False, required=False)
