from django.db import models

from fifa.apps.nations.models import Nation
from fifa.models import TimeStampedModel, EaModel


class League(TimeStampedModel, EaModel):
    name = models.CharField(max_length=255)
    name_abbr = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    nation = models.ForeignKey(Nation, blank=True, null=True)

    image_medium = models.CharField(max_length=500)

    order = models.PositiveIntegerField(default=0)

    # Players
    player_average_rating = models.FloatField(null=True)
    player_count = models.PositiveIntegerField(null=True)
    player_count_special = models.PositiveIntegerField(null=True)
    player_count_gold = models.PositiveIntegerField(null=True)
    player_count_silver = models.PositiveIntegerField(null=True)
    player_count_bronze = models.PositiveIntegerField(null=True)

    class Meta:
        ordering = ('order', 'name', 'pk')
        verbose_name = 'League'
        verbose_name_plural = 'Leagues'

    def __str__(self):
        return self.name

