from django.db import models

from .mechanic import Mechanic
from .vehicle import Vehicle


class ServiceQuerySet(models.QuerySet):
    def less_90(self):
        return self.filter(cost__lt=90)


class ServiceManager(models.Manager):
    def get_queryset(self):
        return ServiceQuerySet(self.model, using=self._db)


class Service(models.Model):
    vehicle = models.ForeignKey(Vehicle, related_name='services', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    cost = models.FloatField()
    date = models.DateField()
    mechanics = models.ManyToManyField(Mechanic, related_name='services')
    objects = ServiceManager()

    class Meta:
        db_table = 'services'

