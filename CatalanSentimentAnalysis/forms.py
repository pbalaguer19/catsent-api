from django.forms import ModelForm
from django import forms
from models import Tweet

class TweetForm(ModelForm):
    class Meta:
        model = Tweet
        exclude = ('date', 'polarity')
        widgets = {
            'tweet': forms.TextInput(attrs={'class': 'subscribe-input', 'placeholder':'Escriu un Tweet...'}),
        }
