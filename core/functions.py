import random
from django.apps import apps
from django.core.exceptions import ValidationError


def generate_trade_id():
    n = str(random.randint(0, 99999999))
    return n.zfill(8)


def validate_unique_id_trade(uuid, id, seller, crypto, amount, price, root):
    trade_model = apps.get_model(app_label='trade', model_name='Trade')
    search_trade_main = trade_model.objects.filter(id=id, main=True)
    if search_trade_main:
        trade_main = trade_model.objects.get(id=id, main=True)
        if uuid != trade_main.uuid:
            if seller != trade_main.seller or crypto != trade_main.crypto or amount != trade_main.amount or \
                    price != trade_main.price or root != trade_main:
                return "This is not possible because the trade has a different sequence"


def validate_main_sequence_trade(uuid, id, main):
    trade_model = apps.get_model(app_label='trade', model_name='Trade')
    search_trades = trade_model.objects.filter(id=id, main=True).count()
    if main and search_trades >= 1:
        trade_main = trade_model.objects.get(id=id, main=True)
        if uuid != trade_main.uuid:
            return "This is not possible because can only one main trade by id"
