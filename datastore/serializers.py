
from rest_framework import serializers

from datastore.models import Crawler, Sentiment


class CrawlerSerializer(serializers.ModelSerializer):
    # Tell django what model and what fields (if none, all) in the model I want to make available to the rest api
    class Meta:
        model = Crawler


class SentimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentiment




