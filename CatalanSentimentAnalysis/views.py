from django.shortcuts import render
from django.utils import timezone

from models import Tweet
from forms import TweetForm
from django.views.generic.edit import CreateView


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
