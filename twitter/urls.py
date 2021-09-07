from twitter import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page),
    path('admin/', admin.site.urls),
]
