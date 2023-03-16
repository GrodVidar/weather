from django.db import models
from datetime import datetime


class HeatIndex(models.Model):
    temperature = models.FloatField()
    humidity = models.IntegerField()
    date = models.DateTimeField(default=datetime.now())
