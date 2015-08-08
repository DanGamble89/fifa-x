from django.core.management.base import BaseCommand

from fifa.helpers.downloader import ClubDownloader


class Command(BaseCommand):
    def handle(self, *args, **options):
        downloader = ClubDownloader()

        downloader.build_clubs()
