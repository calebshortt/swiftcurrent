from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.conf.urls import url

from datastore import models
from datastore.models import Sentiment


def index(request):
    return HttpResponse("Hello, world. You're at the game index.")

def question(request , question_id):
    
    model = Sentiment()
    template_name = 'gameQuestions.html'
    new_model = model.get(model)

    return HttpResponse(new_model.text)

    