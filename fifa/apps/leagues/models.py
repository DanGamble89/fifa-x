from django.db import models

from fifa.apps.nations.models import Nation
from fifa.models import TimeStampedModel, EaModel


class League(TimeStampedModel, EaModel):
    name = models.CharField(max_length=255)
    name_abbr = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    nation = models.ForeignKey(Nation)

    image_medium = models.CharField(max_length=500)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('order', 'name', 'pk')
        verbose_name = 'League'
        verbose_name_plural = 'Leagues'

    def __str__(self):
        return self.name

