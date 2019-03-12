from django.db import models


class MonthlyAvr(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.IntegerField(default=0)
    name = models.TextField()
    month = models.IntegerField(default=0)
    avrTemp = models.FloatField(default=0.0)
    avrSnow = models.FloatField(default=0.0)