from django.urls import path
from . import views

urlpatterns = [
    path('', views.TweetListView.as_view()),
    path('add-tweet/', views.AddTweet.as_view()),
]
