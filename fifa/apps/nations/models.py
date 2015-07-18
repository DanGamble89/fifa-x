from django.db import models

from ...models import TimeStampedModel, EaModel


class Nation(TimeStampedModel, EaModel):
    name = models.CharField(max_length=255)
    name_abbr = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    image_small = models.CharField(max_length=500)
    image_medium = models.CharField(max_length=500)
    image_large = models.CharField(max_length=500)

    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('order', 'name', 'pk')
        verbose_name = 'Nation'
        verbose_name_plural = 'Nations'

    def __str__(self):
        return self.name
