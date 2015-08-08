from django.db import models

from ..leagues.models import League
from fifa.models import TimeStampedModel, EaModel


class Club(TimeStampedModel, EaModel):
    name = models.CharField(max_length=255)
    name_abbr = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    league = models.ForeignKey(League)

    image_dark_small = models.CharField(max_length=500, blank=True)
    image_dark_large = models.CharField(max_length=500, blank=True)
    image_light_small = models.CharField(max_length=500, blank=True)
    image_light_large = models.CharField(max_length=500, blank=True)

    image_medium = models.CharField(max_length=500)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('order', 'name', 'pk')
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'

    def __str__(self):
        return self.name

