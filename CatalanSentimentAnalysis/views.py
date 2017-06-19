from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.urlresolvers import reverse

from models import Tweet
from forms import TweetForm
from django.views.generic.edit import CreateView
from django.views.generic import DetailView
from serializers import TweetSerializer
import json

# Create your views here.
class TweetCreate(CreateView):
    model = Tweet
    template_name = 'CatalanSentimentAnalysis/form.html'
    form_class = TweetForm

    def form_valid(self, form):
        return super(TweetCreate, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TweetCreate, self).get_context_data(**kwargs)
        context['tweets'] = Tweet.objects.filter(date__lte=timezone.now()).order_by('-date')[:10]
        return context

    def get_success_url(self):
        return 'tweet/{}'.format(self.object.id)

class TweetDetail(DetailView):
    model = Tweet
    template_name = 'CatalanSentimentAnalysis/detail.html'

    def get_context_data(self, **kwargs):
        context = super(TweetDetail, self).get_context_data(**kwargs)
        return context

class TweetAPI(APIView):
    def get(self, request, format=None):
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status==status.HTTP_400_BAD_REQUEST)
