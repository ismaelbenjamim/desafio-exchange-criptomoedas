from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.admin.sites import DefaultAdminSite
from django.template.response import TemplateResponse
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import routers, permissions

from core.views import CustomLoginView
from cryptocurrencies.apis.viewsets import CurrencyPairAPI
from mrbit_exchange import settings
from trade.apis.viewsets import SellCryptoAPI, BuyCryptoAPI
from users.apis.viewsets import UserViewSet, UserWalletAPI, UserBalanceAPI

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

router = routers.SimpleRouter()
router.register(r'users/user', UserViewSet)
router.register(r'trades/sell', SellCryptoAPI)
router.register(r'trades/buy', BuyCryptoAPI)


APIs = [
    path('crypto/currency', CurrencyPairAPI.as_view()),
    path('users/user-wallet', UserWalletAPI.as_view()),
    path('users/balance', UserBalanceAPI.as_view())
]

urlpatterns = [
    path('', CustomLoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('apis/', include(router.urls)),
    path('apis/', include(APIs)),
    path(r'swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api-auth/', include('rest_framework.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
