from django.db import models


class Event(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Event Name',
    )
    poster = models.ImageField(
        verbose_name='Poster',
    )
    time_and_date = models.DateTimeField(
        verbose_name='Event time',
    )
    length = models.TimeField(
        verbose_name='Event length',
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Event location',
    )
    information = models.TextField(
        verbose_name='Event information',
    )

    def __str__(self):
        return self.name
