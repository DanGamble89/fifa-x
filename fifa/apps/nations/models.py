from django.db import models

from ...models import TimeStampedModel, EaModel


class Nation(TimeStampedModel, EaModel):
    name = models.CharField(max_length=255)
    name_abbr = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    image_small = models.CharField(max_length=500, blank=True)
    image_medium = models.CharField(max_length=500, blank=True)
    image_large = models.CharField(max_length=500, blank=True)

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
        verbose_name = 'Nation'
        verbose_name_plural = 'Nations'

    def __str__(self):
        return self.name
