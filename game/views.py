from django.shortcuts import render

# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http import HttpResponse ,HttpResponseRedirect
from django.http import Http404
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
    except Sentiment.ObjectDoesNotExist:
        raise Http404("Sentiment does not exsist")
    return render(request , 'game/index.html' , {'question' : value})

def results(request , question_id):
    value = get_object_or_404(Sentiment , id = question_id)
    return render(request , 'game/results.html' , {'question':value })


def vote(request , question_id):
    value = get_object_or_404(Sentiment, id = question_id)
    try:
        selected_choice = Sentiment.choices[0]
    except (KeyError, Sentiment.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'game/detail.html', {
            'Sentiment': value,
            'error_message': "You didn't select a choice.",
        })
    else:
        # selected_choice.votes += 1
        # selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('game:results', args=(request , question_id)))
