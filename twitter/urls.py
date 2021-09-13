from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', include('tweets.urls')),
    path('', include('account.urls')),
    path('', include('message.urls')),
    path('left_menu', views.left_menu, name="left_menu"),
    path('admin/', admin.site.urls),
]
