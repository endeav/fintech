from django.db import models
from django.db.models import CASCADE

from finusers.models import FinUser
from django.utils.translation import ugettext as _


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    ts_create = models.DateTimeField(auto_now_add=True, auto_now=False)
    ts_update = models.DateTimeField(auto_now=True)

    ts_beg = models.DateTimeField(help_text=_('The date of the account activation'))
    ts_end = models.DateTimeField()

    name = models.CharField(max_length=255)
    user = models.ForeignKey(FinUser, related_name='accounts', on_delete=CASCADE)
