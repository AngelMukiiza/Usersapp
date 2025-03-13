from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.urls import reverse

User = get_user_model()  # Get the custom user model

class UserAPITestCase(APITestCase):

    def setUp(self):
        """Set up a test user"""
        self.user = User.objects.create_user(username="testuser", email="test@example.com", password="testpass123")
        self.token = Token.objects.create(user=self.user)  # Create an authentication token
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')  # Authenticate requests with token

        self.user_create_url = reverse("user-list")  # Update based on your URL names
        self.user_detail_url = reverse("user-detail", args=[self.user.id])

    def test_create_user(self):
        """Test creating a user"""
        data = {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "newpass123"
        }
        response = self.client.post(self.user_create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["username"], "newuser")

    def test_get_users(self):
        """Test retrieving users"""
        response = self.client.get(self.user_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)  # Ensure at least one user exists

    def test_get_single_user(self):
        """Test retrieving a single user"""
        response = self.client.get(self.user_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], self.user.username)

    def test_update_user(self):
        """Test updating user details"""
        data = {"username": "updateduser"}
        response = self.client.put(self.user_detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["username"], "updateduser")

    def test_delete_user(self):
        """Test deleting a user"""
        response = self.client.delete(self.user_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
