from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User
# Create your tests here.
class UserResgistrationTest(APITestCase):
    def test_registration(self):
        url = reverse("user_view") #urls.py 에서 지정해 준 url의 name
        user_data = {
            "username" : "testuser",
            "fullname" : "테스터",
            "email" : "test@testuser.com",
            "password" : "password",
        }
        response = self.client.post(url, user_data)
        self.assertEqual(response.data["message"], "가입 완료!!")