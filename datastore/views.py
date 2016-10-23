
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response



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
@api_view(['GET' ,'POST'])
def Sentiment_list(request):

  if request == 'GET':
        Instance = Sentiment.objects.all()
        serializer = SentimentSerializer(Instance,many=True)
        return Response(serializer.Instance)
  elif request == 'POST':
        Instance = SentimentSerializer(Instance = request.Instance)
        if Instance.is_valid():
            Instance.save()
            return Response(Instance.data)
        serializer = SentimentSerializer(Instance,many=True)
        return Response(serializer.data,status=status.HTTP_201_CREATED )
  return Response(status=status.HTTP_404_NOT_FOUND  + "Fuck You MATT")
