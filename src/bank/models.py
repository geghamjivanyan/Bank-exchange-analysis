from django.db import models
from datetime import date
# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField(default=date.today)
    usd_sell = models.FloatField()
    usd_buy = models.FloatField()

    def __str__(self):
        return self.name
