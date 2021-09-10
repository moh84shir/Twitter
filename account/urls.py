from django.urls import path
from . import views

urlpatterns = [
    path('account/signin/', views.SigninView.as_view()),
    path('account/signup/', views.SignupView.as_view()),
    path('account/signout/', views.SignoutView.as_view()),
]