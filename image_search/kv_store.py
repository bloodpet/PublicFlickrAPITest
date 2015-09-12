from django.conf import settings
from redis import StrictRedis
from .exceptions import MissingSettings


def get_connection(name='default'):
    try:
        conn_details = settings.REDIS[name]
    except KeyError:
        raise MissingSettings(name + ' connection not found')
    return StrictRedis(**conn_details)
