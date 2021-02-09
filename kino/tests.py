from django.test import TestCase

from register.models.client import User

from utils import get_avg_age


class AnimalTestCase(TestCase):

    def test_get_avg_age(self):
        users = []
        result = get_avg_age(users)
        self.assertEqual(result, 0)
