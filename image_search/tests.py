from django.test import TestCase


class HomeTestCase(TestCase):

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)
