from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.conf.urls import url
from rest_framework import viewsets

from datastore import models
from datastore.models import Sentiment



class SentimentViewSet(viewsets.ModelViewSet):
    queryset = Sentiment.objects.all()


def index(request):
    return HttpResponse("Hello, world. You're at the game index.")

def question(request , question_id):
    # Sentiment.objects.get(question_id)
    model = Sentiment()
    template_name = 'gameQuestions.html'
    new_model = model.get(model)
    
    output = str(model.num_positive) + ' ' + str(model.num_neutral) + ' ' + str(model.num_negative)
    return HttpResponse( output)

