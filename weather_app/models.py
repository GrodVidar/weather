from django.db import models
from django.utils.timezone import now


class HeatIndex(models.Model):
    temperature = models.FloatField()
    humidity = models.IntegerField()
    date = models.DateTimeField(default=now)
