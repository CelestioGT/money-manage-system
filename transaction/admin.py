from .models import record,AllTeam,MyTeam
from django.contrib import admin

class transactionAdmin(admin.ModelAdmin):
    list_display = ['name','date','description','type','amount']
    list_editable = ['type','amount','description']
admin.site.register(record,transactionAdmin)

class allteamAdmin(admin.ModelAdmin):
    list_display = ['team_id','name','date_build']
    list_editable =['name']
admin.site.register(AllTeam,allteamAdmin)

class myteamAdmin(admin.ModelAdmin):
    list_display = ['team_id','date_join','permissions']
    list_editable =['permissions']
admin.site.register(MyTeam,myteamAdmin)