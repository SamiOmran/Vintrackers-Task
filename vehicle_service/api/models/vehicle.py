from django.db import models
from . import Lead


class Vehicle(models.Model):
    vin = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
