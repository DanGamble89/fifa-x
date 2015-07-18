from django.core import management
from django.core.management.base import BaseCommand

from datetime import datetime
from django.utils.text import slugify

from ...models import Nation

import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        start_time = datetime.now()
        base_url = 'https://www.easports.com/uk/fifa/ultimate-team/api/fut/item'

        total_pages = get_total_pages(base_url)
        request_urls = get_request_urls(total_pages + 1)

        nations = build_data(request_urls)

        for nation in nations:
            nation_data = {
                'name': nation['name'],
                'name_abbr': nation['abbrName'],
                'image_small': nation['smallImgUrl'],
                'image_medium': nation['imgUrl'],
                'ea_id': nation['id']
            }

            obj, created = Nation.objects.get_or_create(**nation_data)

            if created:
                obj.slug = slugify('{}-{}'.format(obj.id, obj.name))
                obj.save()

        print(datetime.now() - start_time)


def get_total_pages(url):
    request = requests.get(url).json()

    return request['totalPages']


def get_request_urls(pages):
    urls = []

    for i in range(1, pages):
        urls.append(
            'https://www.easports.com/uk/fifa/ultimate-team/api/fut/item?jsonParamObject=%7B%22page%22:{}%7D'.format(
                i
            )
        )

    return urls


def build_data(urls):
    nations = []
    urls_to_retry = []

    for i, url in enumerate(urls):
        try:
            request = requests.get(url).json()
            print('Got page {}'.format(url))

            for item in request['items']:
                nation = item['nation']

                if nation not in nations:
                    nations.append(nation)
                    print('Got nation {} ({})'.format(
                        nation['name'],
                        i + 1
                    ))
        except Exception as e:
            print(e)

    return nations
