from django.contrib import admin

from users.models import User, UserWallet

admin.site.register(User)
admin.site.register(UserWallet)
