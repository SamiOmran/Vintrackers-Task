from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

from api.models import Lead


class LeadAPITestCase(TestCase):

    def setUp(self):
        self.client = APIClient()

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

        self.lead = Lead.objects.create(**self.lead_data)
        self.base_url = '/api/leads'

    def test_01_create_lead(self):
        response = self.client.post(self.base_url, self.lead_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['first_name'], self.lead_data['first_name'])

    def test_02_get_lead_list(self):
        response = self.client.get(self.base_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # There's only 1 lead created in `setUp`

    def test_03_get_lead_detail(self):
        response = self.client.get(f'{self.base_url}/{id}/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.lead.first_name)

    def test_04_update_lead(self):
        response = self.client.put(f'{self.base_url}/{self.lead.id}/', self.updated_lead_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['first_name'], self.updated_lead_data['first_name'])
        self.assertEqual(response.data['email'], self.updated_lead_data['email'])

    # def test_05_delete_lead(self):
    #     response = self.client.delete(f'{self.base_url}/{self.lead.id}/', format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     response = self.client.get(f'{self.base_url}/{self.lead.id}/', format='json')
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
