from django.db import models
from .schedule import Schedule


class Ticket(models.Model):
    BOOKING_STATUS = (
        ('FREE', 'free'),
        ('BOOKED', 'booked')
    )

    PLACE_TYPE = (
        ('COMMON', 'common'),
        ('VIP', 'vip')
    )

    row = models.IntegerField(null=False)
    place = models.IntegerField(null=False)
    price = models.IntegerField(null=False)
    status = models.CharField(null=False, choices=BOOKING_STATUS, default='Free')
    type = models.CharField(null=False, choices=PLACE_TYPE)
    schedule = models.ForeignKey(Schedule, null=False, on_delete=models.CASCADE)
