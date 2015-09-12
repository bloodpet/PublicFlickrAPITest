import json
from django.test import TestCase
from django.conf import settings
from .kv_store import get_connection
from .exceptions import MissingSettings


class HomeTestCase(TestCase):

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code)


class SearchViewTest(TestCase):

    def test_get(self):
        response = self.client.get('/search')
        self.assertEqual(200, response.status_code)
        self.assertTrue('items' in response.data.keys())

        response = self.client.get('/search?search_term=')
        self.assertEqual(200, response.status_code)
        self.assertTrue('items' in response.data.keys())


class RedisTest(TestCase):

    def test_missing_connection(self):
        conn_name = 'non-existent'
        self.assertRaisesMessage(
            MissingSettings, conn_name + ' connection not found',
            get_connection, conn_name)

    def test_valid_connection(self):
        conn_name = 'default'
        expected_port = settings.REDIS[conn_name]['port']
        redis = get_connection(conn_name)
        info = redis.info()
        self.assertEqual(expected_port, info['tcp_port'])
