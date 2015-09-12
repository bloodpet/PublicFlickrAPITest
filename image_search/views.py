from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
import requests


def home(request):
    return render(request, template_name='home.html')


class SearchViewSet(APIView):

    def get(self, request):
        flickr_url = 'https://api.flickr.com/services/feeds/photos_public.gne?format=json&nojsoncallback=1'
        resp = requests.get(flickr_url)
        items = resp.json()['items']
        return Response({'items': items})
