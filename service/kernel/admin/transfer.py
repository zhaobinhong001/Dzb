# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from reversion.admin import VersionAdmin
from ..models.transfer import Transfer


class TransferAdmin(VersionAdmin):
    #  list_display = ('name','price')
    # list_editable = ('price',)
    list_display = ('parent_id', 'drawee', 'Payee', 'transfer_type', 'transfer_money', 'receivables_mark')
    pass


admin.site.register(Transfer, TransferAdmin)
