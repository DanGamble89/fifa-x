from django.contrib.staticfiles.storage import staticfiles_storage
from django.template import defaultfilters

from jinja2 import Environment

from fifa.apps.players.views import build_url


def environment(**options):
    env = Environment(**options)

    env.globals.update({
        'static': staticfiles_storage.url,
        # 'url': reverse,
        'url': build_url,
        'dj': defaultfilters
    })

    return env
