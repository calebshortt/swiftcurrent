from django.shortcuts import render

# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.conf.urls import url
from rest_framework import viewsets
from django.template import loader

from datastore import models
from datastore.models import Sentiment



class SentimentViewSet(viewsets.ModelViewSet):
    queryset = Sentiment.objects.all()


def index(request):
    latest_question_list = Sentiment.objects.order_by('-num_positive')[:100]
    template = loader.get_template('game/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
    # value = 'These are all the Sentiments in the database: '
    # SentimentList = Sentiment.objects.order_by('-num_positive')
    # temp = ' '.join([x.text for x in SentimentList])
    # value = value + temp
    # return HttpResponse(value)

def question(request , question_id):

    try:
        title = "The Sentiment we are looking at is %s" , question_id
        value = Sentiment.objects.get(id = question_id)
        # title = title + value.text
        return HttpResponse(value.text)
    except Sentiment.objects.get(id = question_id).ObjectDoesNotExist:
        return HttpResponse("Object not in database...")


