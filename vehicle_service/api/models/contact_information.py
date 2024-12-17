from django.db import models
from . import Lead


class ContactInformation(models.Model):
    id = models.BigAutoField(primary_key=True)
    lead_id = models.ForeignKey(Lead, on_delete=models.CASCADE)
    contact_type = models.CharField(max_length=100)
    contact_value = models.CharField(max_length=100)
