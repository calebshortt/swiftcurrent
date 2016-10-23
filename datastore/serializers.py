
from rest_framework import serializers

from datastore.models import Crawler, Sentiment


class CrawlerSerializer(serializers.ModelSerializer):
    # Tell django what model and what fields (if none, all) in the model I want to make available to the rest api
    class Meta:
        model = Crawler


class SentimentSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Sentiment.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance = validated_data(instance)
        instance.save()
        return instance

    class Meta:
        model = Sentiment




