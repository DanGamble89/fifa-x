from django.core.management.base import BaseCommand

from fifa.helpers.downloader import LeagueDownloader


class Command(BaseCommand):
    def handle(self, *args, **options):
        downloader = LeagueDownloader()

        downloader.build_leagues()
