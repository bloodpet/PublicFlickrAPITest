from django.conf.urls import url
from image_search.views import *

search_view = SearchViewSet.as_view()
like_view = LikeViewSet.as_view()

urlpatterns = [
    url(r'^like/(?P<pk>.+)$', like_view),
    url(r'^search$', search_view),
    url(r'^$', home),
]
