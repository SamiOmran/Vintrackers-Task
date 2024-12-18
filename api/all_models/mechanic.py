from django.db import models


SPECIALIZATIONS = {
    'ER': 'Engine repair',
    'B': 'Brakes',
    'SS': 'Steering and suspension',
    'EP': 'Engine performance',
}


class Mechanic(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=20, choices=SPECIALIZATIONS)

    class Meta:
        db_table = 'mechanics'
