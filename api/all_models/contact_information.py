from django.db import models
from .lead import Lead

CONTACT_TYPES = {
    'ph': 'phone',
    'email': 'email',
    'line': 'telephone',
    'fax': 'fax'
}


class ContactInformation(models.Model):
    id = models.BigAutoField(primary_key=True)
    lead_id = models.ForeignKey(Lead, related_name='contacts_information', on_delete=models.CASCADE)
    contact_type = models.CharField(max_length=10, choices=CONTACT_TYPES)
    contact_value = models.CharField(max_length=100)

    class Meta:
        db_table = 'contacts_information'
