from django.core.exceptions import ValidationError
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from drf_yasg import openapi
from rest_framework.response import Response

from trade.apis.serializers import SellCryptoSerializer, BuyCryptoSerializer, BuyCryptoIDSerializer
from trade.models import Trade


class SellCryptoAPI(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = SellCryptoSerializer
    http_method_names = ['post']
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary='Sell Crypto API')
    def create(self, request, *args, **kwargs):
        return super(SellCryptoAPI, self).create(request, *args, **kwargs)


class BuyCryptoAPI(viewsets.ModelViewSet):
    queryset = Trade.objects.all()
    serializer_class = BuyCryptoIDSerializer
    http_method_names = ['post']
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_summary='Buy Crypto API')
    def create(self, request, *args, **kwargs):
        serializer = BuyCryptoIDSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        get_last_trade = Trade.objects.filter(id=request.data['id']).last()
        if get_last_trade:
            data = {
              "crypto": get_last_trade.crypto.abbreviation,
              "id": get_last_trade.id,
              "status": "Sold out",
              "closed": True,
              "amount": get_last_trade.amount,
              "price": get_last_trade.price,
              "main": False,
              "seller": get_last_trade.seller.uuid,
              "buyer": request.data['user'],
              "root": get_last_trade.uuid
            }
        else:
            return Response({'message': 'This trade ID is not exists'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = BuyCryptoSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
