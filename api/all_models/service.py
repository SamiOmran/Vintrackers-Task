from django.db import models
from .vehicle import Vehicle


class Service(models.Model):
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    cost = models.FloatField()
    date = models.DateField()
