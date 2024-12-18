from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Lead


class LeadAPITestCase(TestCase):

    def setUp(self):
        # Initialize API Client
        self.client = APIClient()

        # Sample lead data
        self.lead_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'joh.ndoe@example.com',
            'phone': '123456789'
        }
        self.updated_lead_data = {
            'first_name': 'Jane',
            'last_name': 'Smith',
            'email': 'jane.smith@example.com',
            'phone': '987654321'
        }

        # Create a test lead
        self.lead = Lead.objects.create(**self.lead_data)
        self.base_url = '/api/leads'

    def test_create_lead(self):
        """Test creating a new lead."""
        response = self.client.post(self.base_url, self.lead_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], self.lead_data['first_name'])
    #
    # def test_get_lead_list(self):
    #     """Test retrieving the list of leads."""
    #     response = self.client.get(self.base_url, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 1)  # There's only 1 lead created in `setUp`
    #
    # def test_get_lead_detail(self):
    #     """Test retrieving a specific lead."""
    #     response = self.client.get(f'{self.base_url}/{self.lead.id}/', format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['first_name'], self.lead.first_name)
    #
    # def test_update_lead(self):
    #     """Test updating an existing lead."""
    #     response = self.client.put(f'{self.base_url}/{self.lead.id}/', self.updated_lead_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['first_name'], self.updated_lead_data['first_name'])
    #     self.assertEqual(response.data['email'], self.updated_lead_data['email'])
    #
    # def test_delete_lead(self):
    #     """Test deleting a lead."""
    #     response = self.client.delete(f'{self.base_url}/{self.lead.id}/', format='json')
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    #
    #     # Verify that the lead is no longer in the database
    #     response = self.client.get(f'{self.base_url}/{self.lead.id}/', format='json')
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
