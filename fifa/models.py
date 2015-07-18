from django.db import models


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class EaModel(models.Model):
    ea_id = models.PositiveIntegerField()

    class Meta:
        abstract = True
