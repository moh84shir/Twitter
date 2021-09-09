from .models import Tweet
from django.views.generic import ListView

class TweetListView(ListView):
    model = Tweet
    template_name = "tweets/tweet_list.html"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     logedin_user = self.request.user
    #     context['user'] = logedin_user
    #     return context
