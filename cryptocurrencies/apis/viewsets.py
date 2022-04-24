from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from cryptocurrencies.apis.external import crypto_compare
from cryptocurrencies.apis.serializers import CurrencyPairSerializer


class CurrencyPairAPI(APIView):
    http_method_names = ['get']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Consuming CryptoCompare API", query_serializer=CurrencyPairSerializer)
    def get(self, request):
        crypto = request.GET.get('crypto')
        currencys = request.GET.get('currencys')
        return crypto_compare(crypto, currencys)
