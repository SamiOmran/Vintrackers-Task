from django.db import models


class Lead(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=30)


class ContactInformation(models.Model):
    id = models.BigAutoField(primary_key=True)
    lead_id = models.ForeignKey(Lead, on_delete=models.CASCADE)
    contact_type = models.CharField(max_length=100)
    contact_value = models.CharField(max_length=100)


class Vehicle(models.Model):
    vin = models.CharField(max_length=100)
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    lead = models.ForeignKey(Lead, on_delete=models.CASCADE)


class Service(models.Model):
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    cost = models.FloatField()
    date = models.DateField()


class Mechanic(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
