from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cryptocurrencies.apis.external import crypto_compare
from cryptocurrencies.models import CryptoWallet
from users.apis.serializers import UserSerializer, UserWalletSerializer, UserBalanceSerializer
from users.models import User, UserWallet


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]


class UserBalanceAPI(APIView):
    http_method_names = ['get']
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Get the user balance", query_serializer=UserBalanceSerializer)
    def get(self, request):
        user_uuid = request.GET.get('uuid')
        user = User.objects.get(uuid=user_uuid)
        user_wallet = UserWallet.objects.get(user=user)

        response = {
            "uuid": user_uuid,
            "name": f"{user.first_name} {user.last_name}",
            "balance": user_wallet.balance,
        }
        return Response(response, status=status.HTTP_200_OK)



class UserWalletAPI(APIView):
    http_method_names = ['get']
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Get the user wallet", query_serializer=UserWalletSerializer)
    def get(self, request):
        user_uuid = request.GET.get('user')
        crypto_in_usd = request.GET.get('crypto_in_usd')
        user = get_object_or_404(User, uuid=user_uuid)
        user_wallet = UserWallet.objects.get(user=user)
        cryptos_wallet = CryptoWallet.objects.filter(user_wallet=user_wallet)

        response = {
            "uuid": user_uuid,
            "name": f"{user.first_name} {user.last_name}",
            "wallet": user_wallet.uuid,
            "cryptos": []
        }
        for crypto in cryptos_wallet:
            add_response = {
                "name": crypto.crypto.name,
                "abbreviation": crypto.crypto.abbreviation,
                "amount": crypto.amount,
            }
            if crypto_in_usd == "true":
                crypto_usd = crypto_compare(crypto.crypto.abbreviation, 'usd')
                value = round(crypto_usd.data.get('USD') * float(crypto.amount), 2)
                add_response["usd"] = value

            response['cryptos'].append(add_response)

        return Response(response, status=status.HTTP_200_OK)
