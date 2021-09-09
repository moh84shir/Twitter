from twitter import views
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('tweets.urls')),
    path('admin/', admin.site.urls),
]
