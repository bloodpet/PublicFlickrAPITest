from django.conf.urls import url
from image_search.views import *

urlpatterns = [
    url(r'$', home),
]
