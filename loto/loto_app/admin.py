from django.contrib import admin

# Register your models here.
from loto.loto_app.models import Team, Player, Bet, Mybet


class BetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'time_to_edit')
    list_filter = ('type', 'time_to_edit')


admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Bet)
admin.site.register(Mybet)