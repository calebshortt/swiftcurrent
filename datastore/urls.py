
from django.conf.urls import url, include
from rest_framework import routers

from datastore.views import CrawlerViewSet, SentimentViewSet

# Tell django how to route the requested url to an actual view that we have created

router = routers.DefaultRouter()

router.register(r'crawlers', CrawlerViewSet)
router.register(r'sentiments', SentimentViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]