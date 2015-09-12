import logging
import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .kv_store import get_connection

log = logging.getLogger(__name__)


def home(request):
    return render(request, template_name='home.html')


class SearchViewSet(APIView):

    def get(self, request):
        flickr_url = 'https://api.flickr.com/services/feeds/photos_public.gne?format=json&nojsoncallback=1'
        if request.GET.get('search_term', ''):
            terms = request.GET['search_term']
            tags = ','.join(terms.split(' '))
            flickr_url += '&tags=' + tags
        resp = requests.get(flickr_url)
        o_items = resp.json()['items']
        items = []
        redis = get_connection('default')
        for item in o_items:
            pk = item['pk'] = item['link'].replace('https://www.flickr.com/photos/', '').\
                    replace('/', '-')
            cnt = redis.get(pk) or 0
            item['likeCount'] = int(cnt)
            items.append(item)
        return Response({'items': items})


class LikeViewSet(APIView):

    def get(self, request, pk):
        redis = get_connection('default')
        cnt = redis.get(pk) or 0
        return Response({'count': int(cnt)})

    def post(self, request, pk):
        redis = get_connection('default')
        redis.incr(pk)
        return Response({'success': True})
