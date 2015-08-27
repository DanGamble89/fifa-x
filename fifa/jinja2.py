from django.contrib.staticfiles.storage import staticfiles_storage
from django.template import defaultfilters

from jinja2 import Environment
from webpack_loader.templatetags.webpack_loader import render_bundle

from .apps.players.views import build_url

import math


def height_imperial(height, labels=False):
    inches, feet = math.modf(height * 0.032808399)

    value = '{}{feet}{}{inches}'.format(
        int(feet), int(round(inches * 12, 1)),
        feet='ft ' if labels else '\'',
        inches='in' if labels else '"'
    )

    return value


def environment(**options):
    env = Environment(**options)

    env.filters['height_imperial'] = height_imperial

    env.globals.update({
        'static': staticfiles_storage.url,
        # 'url': reverse,
        'url': build_url,
        'dj': defaultfilters
    })

    return env
