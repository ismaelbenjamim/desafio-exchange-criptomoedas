import requests
from rest_framework import status
from rest_framework.response import Response


def crypto_compare(crypto_symbol, currencys):
    try:
        response = requests.get(
            url=f'https://min-api.cryptocompare.com/data/price',
            params={
                "fsym": crypto_symbol,
                "tsyms": currencys
            }
        )
        return Response(response.json(), status=response.status_code)
    except:
        return Response({"message": "It's not possible because has a problem in CryptoCompare API."},
                        status=status.HTTP_400_BAD_REQUEST)
