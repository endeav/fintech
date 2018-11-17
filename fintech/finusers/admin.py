from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import FinUser


class FinUserAdmin(DjangoUserAdmin):
    model = FinUser
    list_display = ['email', 'username',]


admin.site.register(FinUser, FinUserAdmin)
