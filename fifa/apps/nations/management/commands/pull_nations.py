from django.conf import settings
from django.core import management
from django.core.management.base import BaseCommand

from datetime import datetime
from django.utils.text import slugify
from fifa.apps.nations.tasks import download_nation, create_nation

from ...models import Nation

import json
import os
import requests
import urllib.request


class Command(BaseCommand):
    def handle(self, *args, **options):
        downloader = Downloader()

        nations = downloader.create_nation()


class Downloader(object):
    base_url = 'https://www.easports.com/uk/fifa/ultimate-team/api/fut/item'

    def __init__(self):
        self.initial_request = requests.get(self.base_url).json()
        self.start_time = datetime.now()

    def get_total_pages(self):
        request = self.initial_request

        return request['totalPages']

    def get_request_urls(self):
        urls = []

        for i in range(1, self.get_total_pages() + 1):
            urls.append(
                'https://www.easports.com/uk/fifa/ultimate-team/api/fut/item?jsonParamObject=%7B%22page%22:{}%7D'.format(
                    i
                )
            )

        return urls

    def get_nation_data(self, urls=None):
        if not urls:
            urls = self.get_request_urls()

        data = []

        for i, url in enumerate(urls):
            print('Trying page {}'.format(i))
            data.append(download_nation.delay(url))

        return data

    def create_nation(self):
        data = self.get_nation_data()

        for nation in data:
            if nation.get():
                if not nation['failed']:
                    create_nation.delay(nation['data'])


    # def get_nation_data(self, urls):
    #     nations = []
    #     urls = urls or self.get_request_urls()
    #     url_fails = []
    #
    #     for i, url in enumerate(urls):
    #         request = requests.get(url)
    #         print('Trying page {}'.format(i))
    #
    #         try:
    #             request_json = request.json()
    #         except Exception as e:
    #             url_fails.append(url)
    #
    #             print(e)
    #
    #             continue
    #
    #         if request.status_code == requests.codes.ok:
    #             for item in request_json['items']:
    #                 nation = item['nation']
    #
    #                 nation_data = {
    #                     'name': nation['name'],
    #                     'name_abbr': nation['abbrName'],
    #                     'ea_id': nation['id'],
    #                     'image_small': nation['smallImgUrl'],
    #                     'image_medium': nation['imgUrl']
    #                 }
    #
    #                 if nation_data not in nations:
    #                     nations.append(nation_data)
    #         else:
    #             url_fails.append(url)
    #
    #         print('Total nations {}'.format(len(nations)))
    #         print('Failed urls {}'.format(len(url_fails)))
    #
    #     while url_fails:
    #         self.get_nation_data(url_fails)

# def get_total_pages(url):
#     request = requests.get(url).json()
#
#     return request['totalPages']
#
#
# def get_request_urls(pages):
#     urls = []
#
#     for i in range(1, pages):
#         urls.append(
#             'https://www.easports.com/uk/fifa/ultimate-team/api/fut/item?jsonParamObject=%7B%22page%22:{}%7D'.format(
#                 i
#             )
#         )
#
#     return urls
#
#
# def download_files(urls):
#     url_whitelist = urls
#
#     while urls:
#         for i, url in enumerate(urls):
#             request = requests.get(url)
#             download_directory = os.path.abspath(
#                 os.path.join(
#                     os.path.dirname(
#                         settings.BASE_DIR
#                     ),
#                     '.tmp',
#                     'files',
#                     'page_{}.json'.format(i)
#                 )
#             )
#
#             if request.status_code != 200:
#                 print('Page errored {} - {}'.format(url, request.status_code))
#             else:
#                 print('Got page {}'.format(url))
#                 urllib.request.urlretrieve(url, download_directory)
#
#                 if retry:
#                     url_fails.remove(url)
#
#
# def build_data(urls):
#     nations = []
#     urls_to_retry = []
#
#     for i, url in enumerate(urls):
#         try:
#             request = requests.get(url).json()
#             print('Got page {}'.format(url))
#
#             for item in request['items']:
#                 nation = item['nation']
#
#                 if nation not in nations:
#                     nations.append(nation)
#                     print('Got nation {} ({})'.format(
#                         nation['name'],
#                         i + 1
#                     ))
#         except Exception as e:
#             print(e)
#
#     return nations
