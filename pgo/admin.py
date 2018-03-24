from __future__ import unicode_literals

from django.contrib import admin

from pgo.models import (
    CPM,
    Move,
    Moveset,
    Pokemon,
    PokemonMove,
    RaidBoss,
    RaidTier,
    Type,
    TypeEffectivness,
    TypeEffectivnessScalar,
    WeatherCondition,
)


class MoveAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )


class PokemonAdmin(admin.ModelAdmin):
    list_display = (
        'number', 'name', 'primary_type', 'secondary_type', 'pgo_stamina',
        'pgo_attack', 'pgo_defense', 'maximum_cp',
    )
    search_fields = (
        'number', 'name',
    )


class RaidBossAdmin(admin.ModelAdmin):
    list_display = (
        'pokemon', 'raid_tier', 'status',
    )
    list_editable = (
        'status',
    )
    search_fields = (
        'pokemon__slug',
    )


admin.site.register(CPM)
admin.site.register(Move, MoveAdmin)
admin.site.register(Moveset)
admin.site.register(Pokemon, PokemonAdmin)
admin.site.register(PokemonMove)
admin.site.register(RaidBoss, RaidBossAdmin)
admin.site.register(RaidTier)
admin.site.register(Type)
admin.site.register(TypeEffectivness)
admin.site.register(TypeEffectivnessScalar)
admin.site.register(WeatherCondition)
