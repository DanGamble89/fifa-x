from django.core.management.base import BaseCommand

from fifa.helpers.downloader import NationDownloader


class Command(BaseCommand):
    def handle(self, *args, **options):
        downloader = NationDownloader()

        downloader.build_nations()
