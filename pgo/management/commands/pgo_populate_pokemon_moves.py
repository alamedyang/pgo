from __future__ import unicode_literals

from decimal import Decimal

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify

from pgo.models import (
    Move,
    PokemonMove,
    Moveset,
)


class Command(BaseCommand):
    help = '''
        Iterate through pokemon movesets and create the PokemonMove objects, then connect them to
        the Moveset object.

        Score moves based on the moveset's weave damage value.
    '''

    def _populate_pokemon_moves(self, moveset):
        moves = moveset.key.split(' - ', 1)
        quick_move = Move.objects.get(slug=slugify(moves[0]))
        cinematic_move = Move.objects.get(slug=slugify(moves[1]))

        moveset.quick_move = self._get_or_create_pokemon_move(moveset, quick_move)
        moveset.cinematic_move = self._get_or_create_pokemon_move(moveset, cinematic_move, True)
        moveset.save()

    def _get_or_create_pokemon_move(self, moveset, move, cinematic=False):
        pokemon = moveset.pokemon

        obj, created = PokemonMove.objects.get_or_create(
            pokemon=moveset.pokemon,
            move=move,
            defaults={
                'stab': True if move.move_type in (
                    pokemon.primary_type, pokemon.secondary_type) else False,
                'score': Decimal(moveset.weave_damage[4][1] / 100)
            }
        )
        if not created:
            obj.stab = True if move.move_type in (
                pokemon.primary_type, pokemon.secondary_type) else False
            obj.score = Decimal(moveset.weave_damage[4][1] / 100)
            obj.save()
        return obj

    def handle(self, *args, **options):
        for moveset in Moveset.objects.all():
            self._populate_pokemon_moves(moveset)