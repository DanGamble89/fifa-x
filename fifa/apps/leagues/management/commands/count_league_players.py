from django.core.management import BaseCommand
from django.db.models import Avg

from ...models import League
from ....players.models import Player


class Command(BaseCommand):
    def handle(self, *args, **options):
        leagues = League.objects.all()

        for league in leagues:
            players = league.player_set.all()

            # Average rating
            league.player_average_rating = '{0:.2f}'.format(list(
                players.aggregate(Avg('overall_rating')).values()
            )[0] or 0)

            # All players
            league.player_count = len(players)

            # All players who aren't rare or standard
            league.player_count_special = Player.objects.filter(
                league=league,
                player_type__in=Player.special_types()
            ).count()

            # All golds
            league.player_count_gold = Player.objects.filter(
                league=league,
                quality='gold'
            ).exclude(
                player_type__in=Player.special_types()
            ).count()

            # All silvers
            league.player_count_silver = Player.objects.filter(
                league=league,
                quality='silver'
            ).exclude(
                player_type__in=Player.special_types()
            ).count()

            # All bronzes
            league.player_count_bronze = Player.objects.filter(
                league=league,
                quality='bronze'
            ).exclude(
                player_type__in=Player.special_types()
            ).count()

            league.save()
