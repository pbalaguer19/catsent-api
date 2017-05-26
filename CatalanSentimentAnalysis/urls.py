from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from models import Tweet
from forms import TweetForm
from views import TweetCreate, TweetDetail, TweetAPI

urlpatterns = [
    # Home
    url(r'^$',
        TweetCreate.as_view(),
        name='tweets'),

    url(r'^tweet/(?P<pk>\d+)/$',
        TweetDetail.as_view(),
        name='tweet_detail'),

    url(r'^api/$',
        TweetAPI.as_view(),
        name='api'),
        ]
urlpatterns = format_suffix_patterns(urlpatterns)
