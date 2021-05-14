from .models import record
from django.contrib import admin

class transactionAdmin(admin.ModelAdmin):
    list_display = ['name','date','description','type','amount']
    list_editable = ['type','amount','description']
admin.site.register(record,transactionAdmin)