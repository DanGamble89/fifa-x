from celery.task import task
from celery.utils.log import get_task_logger
import requests
from fifa.apps.nations.models import Nation

logger = get_task_logger(__name__)


@task(name="Download url")
def download_nation(url):
    request = requests.get(url)

    return_value = {
        'failed': True,
        'data': ''
    }

    logger.info('Downloading url')

    try:
        request_json = request.json()

        return_value['failed'] = False

    except Exception as e:
        print(e)

        return return_value

    if request.status_code == requests.codes.ok:
        for item in request_json['items']:
            nation = item['nation']

            return_value['data'] = {
                'name': nation['name'],
                'name_abbr': nation['abbrName'],
                'ea_id': nation['id'],
                'image_small': nation['smallImgUrl'],
                'image_medium': nation['imgUrl']
            }
    else:
        return return_value

    if not return_value['failed']:
        return Nation.objects.get_or_create(**return_value['data'])

    return return_value


@task(name="Create nation")
def create_nation(data):
    nation, created = Nation.objects.get_or_create(**data)

    return nation, created
