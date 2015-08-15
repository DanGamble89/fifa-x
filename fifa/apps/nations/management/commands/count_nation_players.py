from django.core.management import BaseCommand
from django.db.models import Avg

from ...models import Nation
from ....players.models import Player


class Command(BaseCommand):
    def handle(self, *args, **options):
        nations = Nation.objects.all()

        for nation in nations:
            players = nation.player_set.all()

            # Average rating
            nation.player_average_rating = '{0:.2f}'.format(list(
                players.aggregate(Avg('overall_rating')).values()
            )[0] or 0)

            # All players
            nation.player_count = len(players)

            # All players who aren't rare or standard
            nation.player_count_special = Player.objects.filter(
                nation=nation,
                player_type__in=Player.special_types()
            ).count()

            # All golds
            nation.player_count_gold = Player.objects.filter(
                nation=nation,
                quality='gold'
            ).exclude(
                player_type__in=Player.special_types()
            ).count()

            # All silvers
            nation.player_count_silver = Player.objects.filter(
                nation=nation,
                quality='silver'
            ).exclude(
                player_type__in=Player.special_types()
            ).count()

            # All bronzes
            nation.player_count_bronze = Player.objects.filter(
                nation=nation,
                quality='bronze'
            ).exclude(
                player_type__in=Player.special_types()
            ).count()

            nation.save()
