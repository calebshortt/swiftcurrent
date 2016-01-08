from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.conf.urls import url
from datastore import models

def index(request):
    return HttpResponse("Hello, world. You're at the game index.")


