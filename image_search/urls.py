from django.conf.urls import url
from image_search.views import *

search_view = SearchViewSet.as_view()

urlpatterns = [
    url(r'search$', search_view),
    url(r'$', home),
]
