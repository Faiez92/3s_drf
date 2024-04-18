from django.test import TestCase, Client
from django.urls import reverse
from backend.models import Beneficiary
import json


class BeneficiaryListViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_beneficiaries(self):
        response = self.client.get(reverse('beneficiary_list'))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(response.content, [])

    def test_create_beneficiary(self):
        data = {
            'name': 'John Doe',
            'company': 'XYZ Inc',
            'bank_country': 'US',
            'account_number': '1234567890'
        }
        response = self.client.post(reverse('beneficiary_list'), json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json())
        created_beneficiary = Beneficiary.objects.get(pk=response.json()['id'])
        self.assertEqual(created_beneficiary.name, data['name'])
        self.assertEqual(created_beneficiary.company, data['company'])
        self.assertEqual(created_beneficiary.bank_country, data['bank_country'])
        self.assertEqual(created_beneficiary.account_number, data['account_number'])
