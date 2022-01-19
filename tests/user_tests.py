from rest_framework.test import APITestCase
from django.urls import reverse


class UserTestCase(APITestCase):
    def setUp(self):
        data = {'username': 'admin', 'password': 'admin'}
        self.client.post(reverse('registration'), data=data)

    def test_autherization(self):
        data = {'username': 'admin', 'password': 'admin'}
        response = self.client.post(reverse('token'), data=data)
        self.assertEqual(200, response.status_code)
