from django.db import models
from django.utils import timezone


class Event(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Event Name',
    )
    poster = models.ImageField(
        verbose_name='Poster',
        upload_to='posters/'
    )
    start_time_and_date = models.DateTimeField(
        verbose_name='Event start time/date',
    )
    end_time_and_date = models.DateTimeField(
        verbose_name='Event end time/date',
    )
    location = models.CharField(
        max_length=255,
        verbose_name='Event location',
    )
    information = models.TextField(
        verbose_name='Event information',
    )
    food_provided = models.BooleanField(
        verbose_name='Food Provided',
    )
    points_available = models.BooleanField(
        verbose_name='Points Available',
        default=False,
    )

    RST = 'RST'
    MONASH_SPORT = 'MSPT'
    MRS_EVENT = 'MRS'
    SOCIETY_EVENT = 'HS'
    RST_ONLY = 'STO'

    GROUP_RUNNING_CHOICES = (
        (RST, 'RST Event'),
        (MONASH_SPORT, 'Monash Sport Event'),
        (MRS_EVENT, 'Central MRS Event'),
        (SOCIETY_EVENT, 'Hall Society Event'),
        (RST_ONLY, 'RST ONLY EVENT'),
    )

    group_running = models.CharField(
        max_length=4,
        choices=GROUP_RUNNING_CHOICES,
        default=RST,
    )

    @property
    def length(self):
        return self.end_time_and_date - self.start_time_and_date

    @property
    def currently_running(self):
        now = timezone.now()
        return self.start_time_and_date < now < self.end_time_and_date

    def __str__(self):
        return self.name
