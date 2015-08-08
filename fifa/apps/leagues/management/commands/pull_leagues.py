from django.core.management.base import BaseCommand

from fifa.helpers.downloader import Downloader


class Command(BaseCommand):
    def handle(self, *args, **options):
        downloader = Downloader()

        downloader.build_leagues()
