
from django.shortcuts import render
from rest_framework import viewsets

from datastore.models import Crawler, Sentiment
from datastore.serializers import CrawlerSerializer, SentimentSerializer

# API Views
# Tell the API views where to find the list of objects and what serializer class to use to format the data


class CrawlerViewSet(viewsets.ModelViewSet):
    queryset = Crawler.objects.all()
    serializer_class = CrawlerSerializer


class SentimentViewSet(viewsets.ModelViewSet):
    queryset = Sentiment.objects.all()
    serializer_class = SentimentSerializer


# Other Views