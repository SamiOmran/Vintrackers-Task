from django.db import models

from .mechanic import Mechanic
from .vehicle import Vehicle


class Service(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    cost = models.FloatField()
    date = models.DateField()
    mechanics = models.ManyToManyField(Mechanic, related_name='services')

    class Meta:
        db_table = 'services'
