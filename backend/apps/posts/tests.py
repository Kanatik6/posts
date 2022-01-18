from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory, APITestCase
from django.urls import reverse

from apps.posts.factory import PostFactory
from apps.posts import models

User = get_user_model()


class AuthTestCase(APITestCase):
    def test_registration(self):
        data = {'username': 'admin', 'password': 'admin'}
        response = self.client.post(reverse('registration'), data=data)
        self.assertEqual(200, response.status_code)


class LoginTestCase(APITestCase):
    def setUp(self):
        data = {'username': 'admin', 'password': 'admin'}
        self.client.post(reverse('registration'), data=data)

    def test_autherization(self):
        data = {'username': 'admin', 'password': 'admin'}
        response = self.client.post(reverse('token'), data=data)
        self.assertEqual(200, response.status_code)


class PostTestCase(APITestCase):
    def setUp(self):
        data = {'username': 'admin', 'password': 'admin'}
        response = self.client.post(reverse('registration'), data=data)
        tokens = self.client.post(reverse('token'), data=data)
        token = tokens.json().get('access')
        # print(token)
        self.token = token

    def test_autherization(self):
        data = {'title':'qwe'}
        # print(self.token)
        headers = {'Authorization':'Bearer '+self.token}
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        response = self.client.post(reverse('post-list'), data=data)
    
        print(response.json())
        self.assertEqual(201,response.status_code)
