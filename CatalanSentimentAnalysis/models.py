from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse

from __init__ import *

POLARITY_CHOICES = (
    (1, 'Positive'),
    (-1, 'Negative'),
)

# Create your models here.
class Tweet(models.Model):
    tweet = models.CharField(max_length=140)
    polarity = models.IntegerField(choices=POLARITY_CHOICES, default=1)
    date = models.DateTimeField(default= timezone.now)

    def	__unicode__(self):
        return	u"%s"	%	self.tweet

    def	get_absolute_url(self):
        return	reverse('catalan:tweets')

    def save(self, *args, **kwargs):
        text = cleaner.clean(self.tweet)
        features = dict([(word, True) for word in text.split()])
        predicted = classifier.classify(features)
        if predicted == 'pos':
            self.polarity = 1
        else:
            self.polarity = -1
        super(Tweet, self).save(*args, **kwargs)
