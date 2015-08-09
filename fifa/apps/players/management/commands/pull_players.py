from django.core.management.base import BaseCommand

from fifa.helpers.downloader import PlayerDownloader


class Command(BaseCommand):
    def handle(self, *args, **options):
        downloader = PlayerDownloader()

        downloader.build_players()
