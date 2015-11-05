
from django.db import models


class TextRelations(models.Model):
    rel_from = models.ForeignKey('datastore.Sentiment', related_name='rel_from')
    rel_to = models.ForeignKey('datastore.Sentiment', related_name='rel_to')


class Sentiment(models.Model):
    text = models.CharField(max_length=255, blank=True)
    num_yes = models.IntegerField(default=0)
    num_no = models.IntegerField(default=0)
    num_neutral = models.IntegerField(default=0)