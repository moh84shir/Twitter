from .models import Tweet
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class TweetListView(ListView):
    model = Tweet
    template_name = "tweets/tweet_list.html"

    @method_decorator(login_required(login_url="account/signin"))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        logedin_user = self.request.user
        context['user'] = logedin_user
        return context
