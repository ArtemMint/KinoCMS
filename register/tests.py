import datetime

from django.test import TestCase
from django.utils import timezone

from register.models.client import User
from register.models.client import Client

from utils import get_avg_age


class UserTestCase(TestCase):

    def setUp(self):
        self.user_1 = User.objects.create(
            username='user1',
            email='user1@gmail.com',
            password='admin',
        )
        # self.user_2 = User.objects.create(
        #     username='user2',
        #     email='user2@gmail.com',
        #     password='admin',
        # )
        
        self.client = Client.objects.get(user=self.user_1)
        self.client.birth_date = datetime.datetime(1999,1,15).date()
        self.client.save()
        
        self.users = Client.objects.all()
        self.none_users = Client.objects.none()
        
    def test_get_user_age(self):
        self.assertEqual(self.client.get_age(),22)
        
    def test_get_avg_age_with_users(self):
        self.assertNotEqual(get_avg_age(self.users), 0)

    def test_get_avg_age_with_none_users(self):
        self.assertEqual(get_avg_age(self.none_users), 0)
