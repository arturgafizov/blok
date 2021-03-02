from django.test import TestCase

from .models import User


class UserModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user('users@test.com', 'pass')

    def test_user_str(self):
        email = str(self.user)
        self.assertEqual(email, 'users@test.com')
