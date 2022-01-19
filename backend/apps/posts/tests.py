from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory, APITestCase
from django.urls import reverse

from apps.posts.factory import PostFactory
from apps.posts import models
from apps.posts.urls import router
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
        self.client.post(reverse('registration'), data=data)
        self.token = self.client.post(reverse('token'), data=data).json().get('access')

    def test_create_post(self):
        data = {'title':'qwe'}
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        response = self.client.post(reverse('post-list'), data=data)
        self.assertEqual(201,response.status_code)
        

class LikeTestCase(APITestCase):
    def setUp(self):
        data = {'username': 'admin', 'password': 'admin'}
        self.client.post(reverse('registration'), data=data)
        self.token = self.client.post(reverse('token'), data=data).json().get('access')
        post_data = {'title':'qwe'}
        self.client.credentials(HTTP_AUTHORIZATION='Bearer '+self.token)
        self.post_id = self.client.post(reverse('post-list'), data=post_data).json().get('id')


    def test_set_like(self):
        kwargs = {'pk': self.post_id}
        like_response =  self.client.post(reverse('post-add-like',kwargs=kwargs))
        dislike_response =  self.client.post(reverse('post-add-dislike',kwargs=kwargs))
        message_like = {'message': 'like is added'}
        message_dislike = {'message': 'dislike is added'}
        self.assertEqual(message_like,like_response.json())
        self.assertEqual(message_dislike,dislike_response.json())
        
        # доставка 