import datetime

from django.test import TestCase
from django.test import tag
from django.test.client import Client as Client_
from django.test.client import RequestFactory
from django.utils import timezone

from register.models.client import User
from register.models.client import Client
from register.views.user import *

from utils import get_avg_age


class ClientTest(TestCase):
    """Testing client"""

    def setUp(self):
        """Init a Client, create and login User,
        prepare response for each test.
        """
        # self.client = Client_()
        self.user = User.objects.create_user(
            'admin',
            'nemnovus@gmail.com',
            '2400bt2400',
        )
        self.login = self.client.login(
            username='admin',
            password='2400bt2400',
        )
        self.response = self.client.get(
            '/profile/login/'
        )

    @tag('fast')
    def test_client_get(self):
        """Test GET /profile/login/ and check user
        """
        self.assertEqual(
            self.response.status_code,
            200
        )

    @tag('fast')
    def test_create_and_login_user(self):
        """Test GET /profile/login/ and chech user
        """
        self.assertEqual(
            str(self.response.context['user']),
            'admin'
        )


class RequestFactoryTest(TestCase):
    """Testing views in app
    """

    def setUp(self):
        self.factory = RequestFactory()

    def test_view(self):
        """Test login view
        """
        request = self.factory.get('/profile/login/')
        response = user_login_view(request)
        self.assertEqual(response.status_code, 200)
