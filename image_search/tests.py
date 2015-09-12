import json
from django.test import TestCase


class HomeTestCase(TestCase):

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)


class SearchViewTest(TestCase):

    def test_get(self):
        response = self.client.get('/search')
        self.assertEqual(200, response.status_code)
        self.assertTrue('items' in response.data.keys())
