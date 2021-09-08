from django.shortcuts import render
from tweets.models import Tweet

def home_page(request):
    tweets = Tweet.objects.all()
    context = {
        'tweets' : tweets
    }
    return render(request, 'index.html', context)