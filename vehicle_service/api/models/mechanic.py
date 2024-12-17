from django.db import models


class Mechanic(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
