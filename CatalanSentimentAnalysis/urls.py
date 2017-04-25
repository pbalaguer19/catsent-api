from django.conf.urls import url
from models import Tweet
from forms import TweetForm
from views import TweetCreate

urlpatterns = [
    # Home
    url(r'^$',
        TweetCreate.as_view(),
        name='tweets'),

        ]
