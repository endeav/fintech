from django.contrib import admin

from .models import Account


class AccountAdmin(admin.ModelAdmin):
    model = Account
    list_display = ['ts_beg', 'name',]


admin.site.register(Account, AccountAdmin)
