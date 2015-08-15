from django.core.management import BaseCommand
from django.db.models import Avg

from ...models import Club
from ....players.models import Player


class Command(BaseCommand):
    def handle(self, *args, **options):
        clubs = Club.objects.all()

        for club in clubs:
            players = club.player_set.all()

            # Average rating
            club.player_average_rating = '{0:.2f}'.format(list(
                players.aggregate(Avg('overall_rating')).values()
            )[0] or 0)

            # All players
            club.player_count = len(players)

            # All players who aren't rare or standard
            club.player_count_special = Player.objects.filter(
                club=club,
                player_type__in=Player.special_types()
            ).count()

            # All golds
            club.player_count_gold = Player.objects.filter(
                club=club,
                quality='gold'
            ).exclude(
                player_type__in=Player.special_types()
            ).count()

            # All silvers
            club.player_count_silver = Player.objects.filter(
                club=club,
                quality='silver'
            ).exclude(
                player_type__in=Player.special_types()
            ).count()

            # All bronzes
            club.player_count_bronze = Player.objects.filter(
                club=club,
                quality='bronze'
            ).exclude(
                player_type__in=Player.special_types()
            ).count()

            club.save()
