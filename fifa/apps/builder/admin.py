from django.contrib import admin

from .models import Squad


class SquadLocationInline(admin.TabularInline):
    model = Squad.players.through


@admin.register(Squad)
class SquadAdmin(admin.ModelAdmin):
    inlines = [
        SquadLocationInline
    ]

