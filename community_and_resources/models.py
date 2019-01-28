from django.conf import settings
from django.db import models

class RST(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name='Name',
    )
    picture = models.ImageField(
        upload_to='RA_photos',
        verbose_name='picture',
    )
    email = models.CharField(
        max_length=255,
        verbose_name='email',
        blank=True,
    )
    facebook = models.CharField(
        max_length=255,
        verbose_name='facebook',
        blank=True,
    )
    phone = models.CharField(
        max_length=255,
        verbose_name='phone number',
        blank=True,
    )
    bio = models.TextField(
        verbose_name='bio',
        blank=True,
    )
    COLLEGE_HEAD = 'CH'
    DEPUTY_COLLEGE_HEAD = 'DCH'
    RESIDENTIAL_SUPPORT_ASSISTANT = 'RSA'
    RESIDENT_ADVISOR = 'RA'

    POSITIONS = (
        (COLLEGE_HEAD, 'College Head'),
        (DEPUTY_COLLEGE_HEAD, 'Deputy College Head'),
        (RESIDENTIAL_SUPPORT_ASSISTANT, 'Residential Support Assistant'),
        (RESIDENT_ADVISOR, 'Resident Advisor'),
    )

    position = models.CharField(
        max_length=3,
        choices=POSITIONS,
        default=RESIDENT_ADVISOR,
    )

    WINGS = (
        ('1E', '1E'),
        ('1W', '1W'),
        ('2E', '2E'),
        ('2W', '2W'),
        ('3E', '3E'),
        ('3W', '3W'),
        ('4E', '4E'),
        ('4W', '4W'),
        ('GF', 'Ground Floor')
    )

    wing = models.CharField(
        max_length=2,
        choices=WINGS,
    )

    def __str__(self):
        return self.name


class Points(models.Model):
    event_name = models.CharField(
        max_length=255,
        verbose_name='Event Name',
    )
    report_time = models.TimeField(
        verbose_name='Event Time',
    )
    reporter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    first_floor = models.FloatField(
        verbose_name='1st Floor',
    )
    second_floor = models.FloatField(
        verbose_name='2nd Floor',
    )
    third_floor = models.FloatField(
        verbose_name='3rd Floor',
    )
    fourth_floor = models.FloatField(
        verbose_name='4th Floor',
    )

