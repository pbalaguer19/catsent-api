from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from models import Tweet
from forms import TweetForm
from django.views.generic.edit import CreateView
from serializers import TweetSerializer

class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
@require_http_methods(["GET", "POST"])
def tweets_list(request):
    """
    List all code serie, or create a new serie.
    """
    if request.method == 'GET':
        tweets = Tweet.objects.all()
        serializer = TweetSerializer(tweets, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = TweetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)



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
