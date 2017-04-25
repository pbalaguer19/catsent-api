from __future__ import unicode_literals

from django.db import models
from datetime import datetime
from django.core.urlresolvers import reverse

POLARITY_CHOICES = (
    (1, 'Positive'),
    (-1, 'Negative'),
)

# Create your models here.
class Tweet(models.Model):
    tweet = models.TextField()
    polarity = models.IntegerField(choices=POLARITY_CHOICES)
    classifiedCorrectly = models.BooleanField()
    date = models.DateTimeField(default=datetime.now)

    def	__unicode__(self):
        return	u"%s"	%	self.tweet

    def	get_absolute_url(self):
        return	reverse('catalan:tweets')

    def save(self, *args, **kwargs):
        self.polarity = 1
        self.classifiedCorrectly = True
        super(Tweet, self).save(*args, **kwargs)
