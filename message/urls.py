from django.urls import path
from . import views

urlpatterns = [
    path('send-message/', views.SendMessageView.as_view()),
    path('messages/', views.MessageListView.as_view()),
]
