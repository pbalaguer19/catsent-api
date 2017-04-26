from django.conf.urls import url, include
from models import Tweet
from forms import TweetForm
from views import TweetCreate, tweets_list

urlpatterns = [
    # Home
    url(r'^$',
        TweetCreate.as_view(),
        name='tweets'),

    url(r'^api/$',
        tweets_list,
        name='api'),
        ]
