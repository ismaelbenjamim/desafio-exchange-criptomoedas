from django.contrib.auth.views import LoginView
from django.shortcuts import render
import locale
from django.db.models import Sum
from trade.models import Trade


def admin_index_context():
    trade_all_balance = Trade.objects.all().aggregate(Sum('price'))
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
    trade_balance = locale.currency(trade_all_balance['price__sum'], grouping=True)

    context = {
        'trade_balance': trade_balance
    }
    return context


class CustomLoginView(LoginView):
    template_name = 'admin/login.html'
