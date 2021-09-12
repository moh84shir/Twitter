from django.shortcuts import redirect, render
from .models import Tweet
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from . import forms
from . import models


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


class AddTweet(View):
    form_class = forms.AddTweetForm
    template_name = "tweets/add_tweet.html"
    context = {}


    @method_decorator(login_required(login_url="account/signin"))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        add_tweet_form = self.form_class(request.POST or None)
        self.context["add_tweet_form"] = add_tweet_form
        return render(self.request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        add_tweet_form = self.form_class(request.POST or None)
        if add_tweet_form.is_valid():
            title = add_tweet_form.cleaned_data.get('title')
            text = add_tweet_form.cleaned_data.get('text')
            user = self.request.user
            models.Tweet.objects.create(title=title, user=user, text=text)

            return redirect('/')

        self.context["add_tweet_form"] = add_tweet_form
        return render(self.request, self.template_name, self.context)

